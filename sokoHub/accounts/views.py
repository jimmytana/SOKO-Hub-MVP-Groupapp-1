from accounts.models import CustomUser
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from functools import wraps
from django.http import HttpResponse
# Create your views here.

def getUserType(request):
    print(request.user.customuser)
    return HttpResponse("User:", request.user.customuser)

def productList(request):
    return render(request, 'customer/product_list.html')

def vendor_required(function):
    @wraps(function)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated or get_user_type(request.user) != "vendor":
            return redirect(request.META.get('HTTP_REFERER', 'homepage'))
        return function(request, *args, **kwargs)
    return wrapper

def customer_required(function):
    @wraps(function)
    def wrapper(request, *args, **kwargs):
        print(request.user.customuser)
        if not request.user.is_authenticated or request.user.customuser.user_type != "customer":
            return redirect(request.META.get('HTTP_REFERER', 'homepage'))
        return function(request, *args, **kwargs)
    return wrapper

def vendor_view(request):
    return HttpResponse("This one is protected")

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        email = request.POST.get('email', '').strip()
        user_type = request.POST.get('user_type', '').strip()
        phone = request.POST.get('phone', '').strip()
        location = request.POST.get('location', '').strip()

        if not username:
            return HttpResponse("Username cannot be empty")

        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already taken")

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )

        CustomUser.objects.create(
            user=user,
            user_type=user_type,
            phone=phone,
            location=location
        )
        Login(request)
        return redirect('homepage')
    return render(request, 'registration.html')
def Login(request):
    print("trying to loggin")
    print(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        # authenticate(request, )
        if user is not None:
            login(request, user)
            return redirect("homepage")
        else:
            return render(request, 'login.html', context = { "error" : "Incorrect password or username"})
    else:
        return render(request, 'login.html')


def ViewAllUsers(request):
    users = CustomUser.objects.all()
    return render(request, 'allUsers.html', {'users':users})
def notFound(request):
    return render(request, '404.html')

@vendor_required
@login_required(login_url='login')
def vendorHomepage(request):
    return render(request, 'vendor/homepage.html', context={'user_type': 'vendor'})

@customer_required
@login_required(login_url='login')
def customerHomepage(request):
    return render(request, 'customer/homepage.html', context={'user_type': 'customer'})

def homepage(request):
    if request.user.customuser.user_type == 'vendor':
        return vendorHomepage(request)
    else:
        return customerHomepage(request)

def logout_view(request):
    logout(request)
    return redirect('login')

@vendor_required
@login_required
def Vendor_dashboard(request):
    print("The request has: ", request)
    return render(request, 'vendor/dashboard.html', context={'user_type': 'vendor'})

@customer_required
@login_required
def Customer_dashboard(request):
    print("The request has: ", request)
    return render(request, 'customer/dashboard.html', context={'user_type': 'customer'})

def get_user_type(user):
    try:
        custom_user = CustomUser.objects.get(user=user)
        return custom_user.user_type
    except CustomUser.DoesNotExist:
        return None
def dashboard(request):
    print("request be like: ", request.user.customuser.user_type)
    if(request.user.is_authenticated):
        if(request.user.customuser.user_type == "vendor"):
            return Vendor_dashboard(request)
        else:
            return Customer_dashboard(request)
    else:
        return Login(request)