from django.shortcuts import render
from tasks.models import Task
from django.core.urlresolvers import reverse
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
)

# Create your views here.

class ListTaskView(ListView):
    model = Task
    template_name = 'task_list.html'

class CreateTaskView(CreateView):

    fields = ['task_name', ]
    model = Task
    template_name = 'edit_task.html'

    def get_success_url(self):
        return reverse('tasks-list')

class DeleteTaskView(DeleteView):

    model = Task
    template_name = 'delete_task.html'

    def get_success_url(self):
        return reverse('tasks-list')



