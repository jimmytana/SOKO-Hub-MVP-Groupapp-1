from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from accounts.views import vendor_required

@vendor_required
def addProduct(request):
    if(request.method == 'GET'):
        return render(request, 'addProduct.html')
    elif(request.method == 'POST'):
        print("request: ", request.POST)
        # Product.objects.create(name, description, vendor, price, stock, image, status)
        return HttpResponse("adding product")

@vendor_required 
def allProducts(request):
    products = Product.objects.all()
    return render(request, 'ProductList.html', {'products': products})
