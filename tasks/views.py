from django.shortcuts import render
from tasks.models import Task
from django.views.generic import ListView

# Create your views here.

class ListTaskView(ListView):
    model = Task
    template_name = 'task_list.html'