from django.urls import path
from todoapp.views import index, buy
from django.urls import include

urlpatterns = [
    path('', index),
    path('buy/', buy),
    #path('bye/', include('todoapp.urls')),
]
