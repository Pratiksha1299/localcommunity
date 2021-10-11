from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

@login_required
def profile(request):
    return render(request,'profile.html')

def registration(response):
    if response.method == "POST":
        form=RegisterForm(response.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            username =form.cleaned_data.get("username")
            if User.objects.filter(email=email).exists():
                messages.warning(response,"Email already Exist")
                return redirect('registration')
            else:
                messages.success(response, "Register successfully")
                form.save()
        return redirect('registration')
    else:
        form = RegisterForm()
    return  render(response,"register.html",{"form":form})