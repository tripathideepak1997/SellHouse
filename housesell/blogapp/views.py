from django.shortcuts import render, redirect
from .forms import Registration, UserUpdateProfile
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import UpdateView

# Create your views here.


def fun(request):
    return render(request, 'simple.html', {'form': Registration})


def register(request):

    if request.method == 'POST':
        registration_form = Registration(request.POST, request.FILES)
        if registration_form.is_valid():
            registration_form.save()
            username = registration_form.cleaned_data.get("username")
            messages.success(request, f'Account Created for {username} !')
            return redirect('home:base')
        else:

            errors = registration_form.errors
            return render(request, 'register.html', {'form': Registration, 'errors': errors})
    else:
        registration_form = Registration()

    return render(request, 'register.html', {'form': registration_form})


@login_required
def profile(request):
    if request.method == "POST":
        update_form = UserUpdateProfile(request.POST, request.FILES, instance=request.user)
        print(update_form.errors)
        if update_form.is_valid():
            update_form.save()
            messages.success(request, f'Account has been updated !')
            return redirect('blogapp:profile')
    else:
        update_form = UserUpdateProfile(instance=request.user)
    context = {'u_form': update_form}
    return render(request, 'profile.html', context)


