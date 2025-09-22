from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CycleLog
import calendar
from datetime import date

# Create your views here.


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
