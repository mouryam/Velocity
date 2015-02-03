from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Represents to-do items

class Task(models.Model):

    task_name = models.CharField(max_length=255)

    due_date = models.DateField()

    owner = models.ForeignKey(User, blank=True, null=True)


    def __str__(self):
        return self.task_name + " -- Due: " + str(self.due_date) + "-- owner" + str(self.owner)

    def get_absolute_url(self):
        return reverse('tasks-view', kwargs={'pk' : self.id})