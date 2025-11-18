from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from .models import Product
from accounts.views import vendor_required, customer_required
@vendor_required # This decorator ensures only vendors can access this view
def addProduct(request):
    if(request.method == 'GET'):
        return render(request, 'vendor/add_product.html')
    elif(request.method == 'POST'):
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        image = request.FILES.get('image')
        vendor = request.user.customuser # The vendor is the currently logged-in user
        Product.objects.create(name=name, description=description, vendor=vendor, price=price, stock=stock, image=image)
        return redirect('products:vendor_products')

@vendor_required
def vendor_products(request):
    # This ensures that vendors only see the products they have created.
    vendor = request.user.customuser
    products = Product.objects.filter(vendor=vendor).order_by('-created_at')
    return render(request, 'vendor/product_list.html', {'products': products, 'user_type': 'vendor'})

def customer_products(request): #Here I didn't make it customer_required because even the unlogged in can access this view
    sort_by = request.GET.get('sort_by', 'newest')

    if sort_by == 'price_asc':
        product_list = Product.objects.all().order_by('price')
    elif sort_by == 'price_desc':
        product_list = Product.objects.all().order_by('-price')
    else: 
        product_list = Product.objects.all().order_by('-created_at')

    paginator = Paginator(product_list, 9) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj, 
        'sort_by': sort_by,
        'user_type': 'customer'
    }
    return render(request, 'customer/product_list.html', context)

def allProducts(request):
    if not request.user.is_authenticated:
            return customer_products(request)
    else:
        if(request.user.customuser.user_type == 'vendor'):
            return vendor_products(request)
        else:
            return customer_products(request)
    
def getProduct(request):
    print("the product id is :", id)
    product = get_object_or_404(Product, id=id)
    context = {'product': product}
    return render(request, 'customer/product_details.html', context)