from django.urls import path
from todoapp.views import todo_main
from django.urls import include

urlpatterns = [
    path('', todo_main, name = 'todo_main')

]
