from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render
from tasks.models import Task
from django.core.urlresolvers import reverse
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView,
    DetailView)
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


class CreateTaskView(LoggedInMixin, CreateView):

    fields = ['task_name', 'due_date', 'comment']
    model = Task
    template_name = 'add_task.html'

    def get_success_url(self):
        return reverse('tasks-list')

    def get_context_data(self, **kwargs):

        context = super(CreateTaskView, self).get_context_data(**kwargs)
        context['action'] = reverse('tasks-new')

        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CreateTaskView, self).form_valid(form)


class DeleteTaskView(DeleteView):

    model = Task
    template_name = 'delete_task.html'

    def get_success_url(self):
        return reverse('tasks-list')


class UpdateTaskView(UpdateView):

    fields = ['task_name', 'due_date', 'comment']
    model = Task
    template_name = 'add_task.html'

    def get_success_url(self):
        return reverse('tasks-list')

    def get_context_data(self, **kwargs):

        context = super(UpdateTaskView, self).get_context_data(**kwargs)
        context['action'] = reverse('tasks-edit', kwargs={'pk' : self.get_object().id})

        return context


class TaskView(LoggedInMixin, DetailView):

    model = Task
    template_name = 'task.html'

    def get_object(self, queryset=None):

        if queryset is None:
            queryset = self.get_queryset()

        pk = self.kwargs.get(self.pk_url_kwarg, None)
        queryset = queryset.filter(pk=pk, owner=self.request.user, )

        try:
            obj = queryset.get()
        except ObjectDoesNotExist:
            raise Http404(_(u"No %(verbose_name)s found matching the query") %
                          {'verbose_name': queryset.model._meta.verbose_name})

        return obj







