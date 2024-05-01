from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('taskList', views.taskList, name='taskList'),
    path('addTask', views.addTask, name='addTask'),
]