from django.urls import path
from django.urls import include

from auth_app.views import login_view, registration, user_list, logout_view, login_in_system, delete_user
from todoapp.views import todo_main

urlpatterns = [
    path('login/', login_view, name ='login'),
    path('delete_user/', delete_user, name ='delete_user'),
    path('login_in_system/', login_in_system, name ='login_in_system'),
    path('logout/', logout_view, name ='logout'),
    path('registration/', registration, name = 'registration'),
    path('user_list/', user_list, name = 'user_list'),


]
