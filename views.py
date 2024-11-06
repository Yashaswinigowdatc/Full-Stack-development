from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import localtime, get_fixed_timezone
import datetime
def time_offset(request):
 current_time =datetime.datetime.now()
 time_ahead = current_time + datetime.timedelta(hours=4)
 time_before = current_time - datetime.timedelta(hours=4)
 context = {
 'current_time': current_time,
 'time_ahead': time_ahead,
 'time_before': time_before,
 }
 return render(request, 'timetrackerahead/time_display.html', context)
