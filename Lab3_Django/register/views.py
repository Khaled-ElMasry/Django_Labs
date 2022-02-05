from django.contrib.auth.models import User as MyUser
from django.shortcuts import render
from django.views import View
from .models import User


def adduseradmin(req):
    return render(req, 'register/register.html')


# Create your views here.
class Register(View):
    def get(self, request):
        return render(request, 'register/register.html')

    def post(self, request):
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        usrname = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # to my database
        User.objects.create(user_fname=fname, user_lname=lname, user_usrname=usrname, user_password=password,
                            user_email=email)
        # to admin board
        MyUser.objects.create_user(username=usrname, email=email, password=password,is_staff=True)
        return render(request, 'register/register.html')
