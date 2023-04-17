from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import get_user_model
from django.contrib import messages

from users.forms import LoginForm

def login(request):
    form = LoginForm()
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('add_instagram')
        else:
            form = LoginForm()
            messages.error(request, 'Invalid email or password')
    return render(request, 'login/login_page.html', {"form": form})