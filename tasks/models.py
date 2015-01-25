from django.db import models

# Create your models here.
# Represents to-do items

class Task(models.Model):

    task_name = models.CharField(max_length=255)

    task_completed = False

    due_date = None

    def __str__(self):
        return self.task_name

    def is_complete(self):
        return self.task_completed

    def check_off(self):
        self.task_completed = True

    def rename(self, new_name):
        self.task_name = new_name
