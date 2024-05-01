from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse


from .models import Task
# Create your views here.
   
class NewTaskForm(forms.Form):
    task = forms.CharField(label = "New task")
    priority = forms.CharField(label = "Priority", min_length= 1, max_length = 10)

def index(request):
    return HttpResponse("Hola mundo")

def taskList(request):
    return render(request, "tareas/listTask.html",{
        "tasks":Task.objects.all()
    })

def addTask(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data
            newTask = Task(tarea = task['task'], priority = task['priority'])
            newTask.save()
            return HttpResponseRedirect(reverse("tasks:taskList"))
    
    return render(request, "tareas/addTask.html",{
        "form":NewTaskForm()
    })