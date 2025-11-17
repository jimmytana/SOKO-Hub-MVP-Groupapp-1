from django.shortcuts import render
from django.http import response
from django.shortcuts import render
from functools import wraps
from django.shortcuts import HttpResponse
# Create your views here.
def register(request):
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