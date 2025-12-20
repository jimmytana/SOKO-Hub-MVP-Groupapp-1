<<<<<<< HEAD
from django.shortcuts import render
from django.http import response
from django.shortcuts import render
from functools import wraps
from django.shortcuts import HttpResponse
=======
from accounts.models import CustomUser
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from functools import wraps
from django.http import HttpResponse
from products.models import Product
from orders.models import OrderItem, Order
>>>>>>> 52ccd12724bef1d2e94201d4145ecc697fe91e40
# Create your views here.

def getUserType(request):
    print(request.user.customuser)
    return HttpResponse("User:", request.user.customuser)

def productList(request):
    return render(request, 'customer/product_list.html')

def vendor_required(function):
    @wraps(function)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.user_type != "vendor":
            return redirect(request.META.get('HTTP_REFERER', 'homepage'))
        return function(request, *args, **kwargs)
    return wrapper

def customer_required(function):
    @wraps(function)
    def wrapper(request, *args, **kwargs):
        print(request.user)
        if not request.user.is_authenticated or request.user.user_type != "customer":
            return redirect(request.META.get('HTTP_REFERER', 'homepage'))
        return function(request, *args, **kwargs)
    return wrapper

def vendor_view(request):
    return HttpResponse("This one is protected")

def register(request):
<<<<<<< HEAD
    return render(request, '../templates/registration.html')

def vendor_required(function):
    @wraps(function)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponse("None")
        return wrapper(request, *args, **kwargs)
    
@vendor_required
def admin(request):
    return HttpResponse("This one is protected")
=======
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        email = request.POST.get('email', '').strip()
        user_type = request.POST.get('user_type', '').strip()
        phone = request.POST.get('phone', '').strip()
        location = request.POST.get('location', '').strip()

        if not username:
            return HttpResponse("Username cannot be empty")

        if CustomUser.objects.filter(username=username).exists():
            return HttpResponse("Username already taken")

        usr = CustomUser.objects.create_user(
            user_type=user_type,
            phone=phone,
            location=location,
            username=username,
            email=email,
            password=password
        )
        Login(request)
        return redirect('homepage')
    return render(request, 'registration.html')
def Login(request):
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

def customerHomepage(request):
    newest_products = Product.objects.order_by('-created_at')[:4]
    return render(request, 'customer/homepage.html', context={'user_type': 'customer', 'newest_products': newest_products})

def homepage(request):
    if request.user.is_authenticated:
        if request.user.user_type == 'vendor':
            return vendorHomepage(request)
        else:
            return customerHomepage(request)
    else:
            return customerHomepage(request)

def logout_view(request):
    logout(request)
    return redirect('login')

@vendor_required
@login_required
def dashboard(request):

    total_products = Product.objects.filter(vendor=request.user).count()

    active_products = Product.objects.filter(vendor=request.user, stock__gt=0).count()

    out_of_stock = Product.objects.filter(vendor=request.user, stock=0).count()

    # pending_orders = Order.objects.filter(vendor=request.user, status='pending').count()
    order_items = OrderItem.objects.all()
    pending_orders = Order.objects.filter(
    orderitem__product__vendor=request.user, 
    status='pending'
).distinct().count()

    context = {
        'order_items': order_items, # You already had this
        'total_products': total_products,
        'active_products': active_products,
        'out_of_stock': out_of_stock,
        'pending_orders': pending_orders,
    }

    return render(request, 'vendor/dashboard.html', context={'user_type': 'vendor', 'order_items': order_items, # You already had this
        'total_products': total_products,
        'active_products': active_products,
        'out_of_stock': out_of_stock,
        'pending_orders': pending_orders,})

def get_user_type(user):
    try:
        custom_user = CustomUser.objects.get(user=user)
        return custom_user.user_type
    except CustomUser.DoesNotExist:
        return None
>>>>>>> 52ccd12724bef1d2e94201d4145ecc697fe91e40
