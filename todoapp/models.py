from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class TodoList(models.Model):
    id = models.IntegerField(primary_key=True) # вставляется само по умолчанию
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()

class TodoStatus(models.Model):
    name = models.TextField()
    C_COMPLETED = 1
    C_NOT_COMPLETED = 2
    C_OVERDUED = 3
    C_CANCELED = 4

class TodoTask(models.Model):
    todo_list = models.ForeignKey(TodoList, models.CASCADE)
    create_at = models.DateTimeField()
    complete_at = models.DateTimeField(null=True)
    status = models.ForeignKey(TodoStatus, models.CASCADE)
    title = models.TextField()
    text = models.TextField()