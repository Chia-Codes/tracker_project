# Django Imports
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_GET

import csv
import os

# Cycle Log Imports
from .models import CycleLog, UserSheet
from .forms import CycleLogForm

# Utilities
import calendar
from datetime import date
from django.contrib import messages
from .google_sheets import fetch_sheet_rows


# Create your views here.
# 500 Something went wrong error
@staff_member_required
@require_GET
def boom_500(request):
    raise RuntimeError("Diagnostic 500: intentional crash for testing")


# Community 
def community(request):
    return render(request, 'tracker/community.html')


# Resources 
def sources(request):
    sheet_id = os.getenv("GOOGLE_RESOURCES_SHEET_ID")
    worksheet = os.getenv("GOOGLE_RESOURCES_WORKSHEET", "Resources")

    resources = []
    if sheet_id:
        try:
            records = fetch_sheet_rows(sheet_id, worksheet)
            # normalise header variations 
            normalised = []
            for r in records:
                normalised.append({
                    'title': r.get('Title') or r.get('title') or r.get('NAME') or '',
                    'description': r.get('Description') or r.get('Desc') or r.get('description') or '',
                    'url': r.get('URL') or r.get('Link') or r.get('link') or '',
                    'image': r.get('Image') or r.get('image') or '',
                    'tag': r.get('Tag') or r.get('tag') or '',
                })
            resources = normalised

        except Exception as e:
            messages.error(request, "Could not load resources from Google Sheets.")
            resources = []
    else:
        messages.info(request, "Set GOOGLE_RESOURCES_SHEET_ID to show resources.")

    return render(request, 'tracker/sources.html', {'resources': resources})


# Journey
def journey(request):
    return render(request, 'tracker/journey.html')


# CSV Export 
@login_required
def export_entries_csv(request):
    """Download the current user's logs as CSV."""
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="trackher_entries.csv"'

    writer = csv.writer(response)
    writer.writerow(['date', 'symptom', 'notes'])

    qs = CycleLog.objects.filter(user=request.user).order_by('-date')
    for log in qs:
        writer.writerow([log.date.isoformat(), log.symptom, log.notes])

    return response


# Tracker View
@login_required
def tracker_view(request):
    today = date.today()
    year = today.year
    month = today.month

    cal = calendar.Calendar(firstweekday=6)
    month_days = cal.monthdatescalendar(year, month)

    if request.method == "POST":
        selected_days = request.POST.getlist("log_days")
        for day_str in selected_days:
            log_date = date.fromisoformat(day_str)
            CycleLog.objects.get_or_create(user=request.user, date=log_date, defaults={'symptom': 'Flow', 'notes': ''})
        return redirect('tracker')  # Redirect to clear form after logging

    user_logs = CycleLog.objects.filter(user=request.user, date__year=year, date__month=month)
    logged_dates = {log.date for log in user_logs}

    context = {
        'month_days': month_days,
        'year': year,
        'month': month,
        'logged_dates': logged_dates,
    }
    return render(request, 'tracker/tracker.html', context)


# Cycle Log Form View
@login_required
def cycle_log_form_view(request):
    if request.method == 'POST':
        form = CycleLogForm(request.POST)
        if form.is_valid():
            user_sheet, created = UserSheet.objects.get_or_create(user=request.user)
            if created:
                sheet_id = create_user_sheet(request.user.username)
                user_sheet.sheet_id = sheet_id
                user_sheet.save()
            else:
                form = CycleLogForm()
            return redirect('tracker')
    else:
        form = CycleLogForm() # Empty form for GET request
    return render(request, 'tracker/cycle_log_form.html', {'form': form})


# Submit Log View
@login_required
def submit_log(request):
    if request.method == 'POST':
        form = CycleLogForm(request.POST)
        if form.is_valid():
            cycle_log = form.save(commit=False)
            cycle_log.user = request.user
            cycle_log.save()
            return redirect('tracker')
    else:
        form = CycleLogForm()
    return render(request, 'tracker/cycle_log_form.html', {'form': form})