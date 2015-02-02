from django.shortcuts import render
from tasks.models import Task
from django.core.urlresolvers import reverse
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView,
)

# Create your views here.

class ListTaskView(ListView):
    model = Task
    template_name = 'task_list.html'

class CreateTaskView(CreateView):

    fields = ['task_name', 'due_date', ]
    model = Task
    template_name = 'add_task.html'

    def get_success_url(self):
        return reverse('tasks-list')

    def get_context_data(self, **kwargs):

        context = super(CreateTaskView, self).get_context_data(**kwargs)
        context['action'] = reverse('tasks-new')

        return context

class DeleteTaskView(DeleteView):

    model = Task
    template_name = 'delete_task.html'

    def get_success_url(self):
        return reverse('tasks-list')


class UpdateTaskView(UpdateView):

    fields = ['task_name', 'due_date', ]
    model = Task
    template_name = 'add_task.html'

    def get_success_url(self):
        return reverse('tasks-list')

    def get_context_data(self, **kwargs):

        context = super(UpdateTaskView, self).get_context_data(**kwargs)
        context['action'] = reverse('tasks-edit', kwargs={'pk' : self.get_object().id})

        return context
