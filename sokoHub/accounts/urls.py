from django.urls import path
from .views import register, Login, ViewAllUsers, homepage, logout_view, vendor_view, dashboard
urlpatterns = [
    path('', homepage),
    path('protected', vendor_view),
    path('register', register, name='register'),
    path('login', Login,name='login'),
    # path('', notFound),
    path('users', ViewAllUsers),
    path('home', homepage, name='homepage'),
    path('logout', logout_view, name='logout'),
    path('dashboard', dashboard, name='dashboard'),
]
