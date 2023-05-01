from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect


def login_view(request: WSGIRequest):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        next_page = request.GET.get('next')


        user: User = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, 'login.html', {
                'error_message': 'Неправильный логин или пароль'
            })
        login(request, user)

        if next_page is not None:
           return redirect(next_page)

        return render(request, 'info.html', {'content': 'Вы вошли в систему'})
    return render(request, 'login.html')


def registration(request: WSGIRequest):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        email = request.POST['email']

        if User.objects.filter(username=username).exists():
            return render(request, 'registration.html', {
                'error_message': 'Пользователь с таким именем уже существует'})

        if password != password_confirm:
            return render(request, 'registration.html', {
                'error_message': 'Пароли не совпадают'
            })
        if len(password) < 10:
            return render(request, 'registration.html', {
                'error_message': 'Пароль слишком короткий'})

        if password != password_confirm:
            return render(request, 'registration.html', {
                'error_message': 'Пароли не совпадают'
            })

        if User.objects.filter(email=email).exists():
            return render(request, 'registration.html', {
                'error_message': 'Пользователь с таким email уже существует'})

        user = User()
        user.username = username
        user.set_password(password)
        user.email = email
        try:
            user.save()
            login(request, user)
        except Exception as e:
            return render(request, 'registration.html', {
                'error_message': 'Ошибка сервера, повторите позднее'})

        return render(request, 'info.html', {'content': 'Регистрация прошла успешно'})
    return render(request, 'registration.html')


def user_list(request: WSGIRequest):
    if not request.user.is_superuser:
        return render(request, 'info.html', {'content': 'Недостаточно прав'})

    users = User.objects.all()
    return render(request, 'user_list.html', {
        'users': users
    })


def logout_view(request: WSGIRequest):
    logout(request)
    return redirect('login')


def login_in_system(request: WSGIRequest):
    user = User.objects.get(pk=request.POST.get("user_id"))
    user1 = User.objects.all()
    print(user1)
    login(request, user)
    return redirect('login')


def delete_user(request: WSGIRequest):
    user = User.objects.get(pk=request.POST.get("user_id"))
    user.delete()
    return redirect('user_list')
