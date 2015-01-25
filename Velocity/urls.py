from django.conf.urls import include, url
from django.contrib import admin
import tasks.views

urlpatterns = [
    # Examples:
    # url(r'^$', 'Velocity.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', tasks.views.ListTaskView.as_view(), name='tasks-list')
]
