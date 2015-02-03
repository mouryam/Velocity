from django.shortcuts import render
from tasks.models import Task
from django.core.urlresolvers import reverse
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView,
)
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.


class LoggedInMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)


class ListTaskView(LoggedInMixin, ListView):
    model = Task
    template_name = 'task_list.html'

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

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



