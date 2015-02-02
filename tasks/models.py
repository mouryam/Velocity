from django.db import models

# Create your models here.
# Represents to-do items

class Task(models.Model):

    task_name = models.CharField(max_length=255)

    due_date = models.DateField()

    def __str__(self):
        return self.task_name + " -- Due: " + str(self.due_date)

