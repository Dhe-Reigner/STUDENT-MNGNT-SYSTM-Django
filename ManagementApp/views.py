from django.shortcuts import render
from . models import Student

def home(request):
    return render(request, 'students/index.html',{
        'students':Student.objects.all()
    })