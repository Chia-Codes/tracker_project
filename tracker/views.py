# Django Imports
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Cycle Log Imports
from .models import CycleLog, UserSheet
from .forms import CycleLogForm
# Google Sheets Imports
from .google_sheets import create_user_sheet

# Utilities
import calendar
from datetime import date


# Create your views here.
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