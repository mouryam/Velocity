from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import tasks.views

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    # Examples:
    # url(r'^$', 'Velocity.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', tasks.views.ListTaskView.as_view(), name='tasks-list'),
    url(r'^new$', tasks.views.CreateTaskView.as_view(), name='tasks-new',),
    url(r'^delete/(?P<pk>\d+)/$', tasks.views.DeleteTaskView.as_view(), name='tasks-delete',),
    url(r'^edit/(?P<pk>\d+)/$', tasks.views.UpdateTaskView.as_view(), name='tasks-edit'),
    url(r'^(?P<pk>\d+)/$', tasks.views.TaskView.as_view(), name='tasks-view',),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),


]

urlpatterns += staticfiles_urlpatterns()