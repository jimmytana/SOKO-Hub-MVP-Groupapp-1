from django.urls import path
from .views import register, Login, ViewAllUsers, homepage, logout_view
urlpatterns = [
    path('', register),
    path('protected', ),
    path('register', register, name='register'),
    path('login', Login,name='login'),
    # path('', notFound),
    path('users', ViewAllUsers),
    path('home', homepage, name='homepage'),
    path('logout', logout_view, name='logout'),
]
