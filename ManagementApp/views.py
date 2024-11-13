from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from . models import Student

def home(request):
    return render(request, 'students/index.html',{
        'students':Student.objects.all()
    })
def view_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse("index"))