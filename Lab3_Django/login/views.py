from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View

from register.models import User
from .forms import LoginForm


# Create your views here.
class Login(View):
    form = LoginForm()

    def get(self, request):
        return render(request, 'login/login.html', {'form': Login.form})

    def post(self, request):
        user_name = request.POST['username']
        user_pass = request.POST['password']
        authuser = authenticate(username=user_name, password=user_pass)
        user = User.objects.filter(user_usrname=user_name, user_password=user_pass)
        if user is not None and authuser is not None:
            login(request, authuser)
            request.session['username'] = user_name  # across web pages
            return redirect('home')
        else:
            messages.success(request, "Invalid Username or Password")
            return render(request, 'login/login.html', {'form': Login.form})

        # user = MyUser.objects.get(user_email=user_mail, user_password=user_pass)
        # if user:
        #     return render(request, 'home/index.html', {'name': 'hamo'})
        # else:
        #     return render(request, 'login/login.html')


def logout_view(request):
    logout(request)
    request.session.clear()
    return redirect('home')
