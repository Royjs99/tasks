from django.shortcuts import render
from django.http import HttpResponse

from .models import Task
# Create your views here.

def index(request):
    return HttpResponse("Hola mundo")

def taskList(request):
    return render(request, "tareas/listTask.html",{
        "tasks":Task.objects.all()
    })

def addTask(request):
    return render(request, 'tareas/addTask.html')

def saveTask(request):
    return