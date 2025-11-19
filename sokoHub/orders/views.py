from django.shortcuts import render
from products.models import Product
from accounts.models import CustomUser
from accounts.views import customer_required, vendor_required
from .models import Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
# Create your views here.
@login_required(login_url='login')
def checkout(request):
    form = {}
    form['price'] = request.POST['price']
    form['quantity'] = request.POST['quantity']
    form['product_id'] = request.POST['product_id']
    print("Current user: ",request.user.id)
    customer = CustomUser.objects.get(id=request.user.id)
    print(customer.email)
    product = Product.objects.get(id=form['product_id'])
    form['phone'] = customer.phone
    form['product_name'] = product.name
    form['address'] = customer.location
    form['sub_total'] = float(form['price']) * float(form['quantity'])
    if request.method == 'POST':
        return render(request, 'order/checkout.html', {'user_type': 'customer', 'form': form, 'product': product, 'email': customer.email, 'customer': customer})
    else:
        redirect('checkout')

@login_required(login_url='login')
def placeOrder(request):
    print(request.POST)
    order = Order.objects.create(customer=request.user,status='pending', total = float(request.POST['total']), delivery_address=request.POST['address'], phone=request.POST['phone'])
    orderItem = OrderItem.objects.create(order=order, product=Product.objects.get(id=request.POST['product_id']), quantity=request.POST['quantity'], price=float(request.POST['price']))
    return render(request, 'order/orderConfirmation.html', {'user_type': 'customer', 'order': order, 'orderItem': orderItem, 'order_items': [Product.objects.get(id=request.POST['product_id'])]})


@login_required
@customer_required 
def myOrders(request):
    orders = Order.objects.filter(customer=request.user)
    return render(request, 'order/orderHistory.html', {'user_type': 'customer', 'orders': orders})


@login_required(login_url='login')
@vendor_required
def vendorOrders(request):
    # orders = Order.objects.filter(customer=request.user)
    orders = Order.objects.all()
    return render(request, 'vendor/orders.html', {'user_type': 'vendor', 'orders': orders})