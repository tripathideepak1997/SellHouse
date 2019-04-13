from django.shortcuts import render, redirect

from blogapp.models import User
from home.models import Enquiry
from property.models import Property
from .forms import Registration, UserUpdateProfile
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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


@login_required
def view_enquiries(request):
    try:
        enquire_obj = Enquiry.objects.filter(person=request.user)
    except Enquiry.DoesNotExist:
        return HttpResponse("<h1>You don't have any enquiries so far </h1>")

    try:
        property_obj = []
        user_obj = []
        for objects in enquire_obj:
            property_obj.append(Property.objects.get(id=objects.property.id))
            user_obj.append(User.objects.get(id=objects.person.id))
    except (Property.DoesNotExist,User.DoesNotExist):
        return HttpResponse("<h1>The property and user does not exist for this enquiry")

    prop_and_user_obj = list(zip(property_obj, user_obj, enquire_obj))
    context = {
        'prop_user': prop_and_user_obj,
    }

    return render(request, 'enquire_view.html', context)


def property_view_enquire(request, id):
    try:
        property_obj = Property.objects.get(id=id)
    except Property.DoesNotExist:
        return HttpResponse("<h1>The Property Does not exist you are requesting for !!!!! sorry trying through url")

    return render(request, 'property_inside.html', {'property': property_obj})
