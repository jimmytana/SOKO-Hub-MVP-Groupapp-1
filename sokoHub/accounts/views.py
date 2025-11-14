from django.shortcuts import render
from django.http import response
from django.shortcuts import render
# Create your views here.
def register(request):
    return render(request, '../templates/registration.html')