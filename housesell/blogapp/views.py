from django.shortcuts import render, redirect
from .forms import Registration
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import View

# Create your views here.


def fun(request):
    return render(request, 'simple.html', {'form': Registration})


def register(request):

    if request.method == 'POST':
        registration_form = Registration(request.POST, request.FILES)
        if registration_form.is_valid():
            registration_form.save()
            username = registration_form.cleaned_data.get("username")
            # first_name = form.cleaned_data.get("first_name")
            # last_name = form.cleaned_data.get("last_name")
            # email_id = form.cleaned_data.get("email_id")
            # password1 = form.cleaned_data.get("password1")
            # password2 = form.cleaned_data.get("password2")
            # is_seller = form.cleaned_data.get("is_seller")
            # description = form.cleaned_data.get("description")
            # photo = form.cleaned_data.get("photo")
            messages.success(request, f'Account Created for {username} !')
            return redirect('blogapp:success_page')
        else:

            errors = registration_form.errors
            return render(request, 'register.html', {'form': Registration, 'errors': errors})
    else:
        form = Registration()

    return render(request, 'register.html', {'form': Registration})


@login_required
def profile(request):
    return render(request, 'profile.html')
