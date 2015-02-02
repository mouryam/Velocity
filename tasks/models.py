from django.db import models

# Create your models here.
# Represents to-do items

class Task(models.Model):

    task_name = models.CharField(max_length=255)

    task_completed = False

    due_date = None

    def __str__(self):
        return self.task_name

