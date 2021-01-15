from django.shortcuts import render

from .models import Job

def home(request):
    Jobs = Job.objects
    return render(request, 'Jobs/home.html', {'Jobs':Jobs})
