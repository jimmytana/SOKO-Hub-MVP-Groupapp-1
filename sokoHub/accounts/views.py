from django.shortcuts import render
from django.http import response
from accounts.models import CustomUser
from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def register(request):
    print("The user was created successfully!!")
    if request.method == 'POST':
        #<======taking input from form ==========>
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']        
        user_type = request.POST['user_type']
        phone = request.POST['phone']
        location = request.POST['location']
        print(username, password, email, user_type, phone, location)
        #<====== inserting data into db ==========>
        try:
            user = User.objects.create_user(username=username, password=password, email=email)
            CustomUser.objects.create( user, user_type=user_type, phone=phone, location=location) 
            print("The user was created successfully!!")
        except Exception:
            print("The user was not created")
            raise
           
    return render(request, '../templates/registration.html')
def login(request):
    return render(request, '../templates/login.html')

def ViewAllUsers(request):
    users = CustomUser.objects.all()
    return render(request, '../templates/allUsers.html', {'users':users})