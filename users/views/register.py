from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from django.contrib import messages

from users.forms import RegisterForm

User = get_user_model()

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'register/register_page.html', {'form': form})