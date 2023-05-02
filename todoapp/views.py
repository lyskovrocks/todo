from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from todoapp.models import TodoStatus, TodoTask, TodoList


# Create your views here.

def todo_main(request):
    if request.method == 'POST':
        action_type = request.POST.get('type')
        if action_type == 'create':
            todo = TodoTask()
            todo.title = request.POST.get('title')
            todo.status = TodoStatus.objects.get(pk=TodoStatus.C_NOT_COMPLETED)
            todo.create_at = datetime.now()
            todo.text = ''
            todo.todo_list = TodoList.objects.get(pk=1)
            todo.save()
        if action_type == 'destroy':
            task_id = request.POST.get('task_id')
            TodoTask.objects.get(pk=task_id).delete()



    todo_list = TodoTask.objects.all().order_by('-id')
    return render(request, 'todo_main.html', {
        'tasks_array': todo_list,
        'todo_count': todo_list.count()
    })


