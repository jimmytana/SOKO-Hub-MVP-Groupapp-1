from django.urls import path
from .views import register, login, ViewAllUsers
urlpatterns = [
    path('register', register),
    path('login', login),
    path('users', ViewAllUsers),
]
