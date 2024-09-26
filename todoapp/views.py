from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from todoapp.models import TodoStatus, TodoTask, TodoList


# Create your views here.



def todo_main(request):
    if request.method == 'POST':
        action_type = request.POST.get('type')
        if action_type == 'create':
            __create_task(request)

        if action_type == 'clear':
            __clear_completed(request)

        if action_type == 'destroy':
            TodoTask.objects.get(pk=request.POST.get('task_id')).delete()
    else:
        action_type = request.GET.get('type')
        if action_type == 'change':
            __chang_todo_status(request)
            
    tasks = TodoTask.objects.filter(todo_list__user=request.user)
    if request.GET.get('status') == 'yes':
        tasks = tasks.filter(status_id=TodoStatus.C_COMPLETED)
    elif request.GET.get('status') == 'no':
        tasks = tasks.filter(status_id=TodoStatus.C_NOT_COMPLETED)

    return render(request, 'todo_main.html', {
        'tasks_array': tasks.order_by('-id'),
        'todo_count': tasks.count()
    })

def __chang_todo_status(request):
    task = TodoTask.objects.get(pk=request.GET.get('task_id'))
    if task.status == TodoStatus.objects.get(pk=TodoStatus.C_NOT_COMPLETED):
        task.status = TodoStatus.objects.get(pk=TodoStatus.C_COMPLETED)
    else:
        task.status = TodoStatus.objects.get(pk=TodoStatus.C_NOT_COMPLETED)
    task.save()

def __create_task(request):
    print('*********************Start creating task**********************')
    todo_list = TodoList.objects.filter(user=request.user).first()
    if todo_list is None:
        print('*********************todo_list is None**********************')
        todo_list = TodoList(user=request.user, date=datetime.now())
        todo_list.save()
        print('New todolist was created')

    todo = TodoTask()
    todo.title = request.POST.get('title')
    todo.status = TodoStatus.objects.get(pk=TodoStatus.C_NOT_COMPLETED)
    # 1todo.create_at = datetime.now()
    todo.text = ''
    todo.todo_list = todo_list
    todo.save()

def __clear_completed(request):
    tasks = TodoTask.objects\
        .filter(todo_list__user=request.user)\
        .filter(status_id=TodoStatus.C_COMPLETED)\
        .delete()
    pass



