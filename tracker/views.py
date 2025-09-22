from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import CycleLog

# Create your views here.


@login_required
def tracker_view(request):
    from .models import CycleLog
    return render(request, 'tracker/tracker.html')
