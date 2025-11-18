from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from functools import wraps

def vendor_required(function):
    @wraps(function)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponse("None")
        return function(request, *args, **kwargs)
    return wrapper
def addProduct(request):
    if(request.method == 'GET'):
        return render(request, 'addProduct.html')
    elif(request.method == 'POST'):
        print("request: ", request.POST)
        # Product.objects.create(name, description, vendor, price, stock, image, status)
        return HttpResponse("adding product")
    
def allProducts(request):
    # products = Product.objects.all()
    return render(request, 'ProductList.html')
