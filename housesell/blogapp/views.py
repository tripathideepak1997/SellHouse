from django.shortcuts import render
from .forms import Registration
from django.http import HttpResponse
# Create your views here.


def fun(request):
    return render(request, 'simple.html', {'form': Registration})


def register(request):
    if request.method == 'GET':
        return render(request, 'index.html', {'form': Registration})
    elif request.method == 'POST':
        form = Registration(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            email_id = form.cleaned_data.get("email_id")
            password1 = form.cleaned_data.get("password1")
            password2 = form.cleaned_data.get("password2")
            is_seller = form.cleaned_data.get("is_seller")
            description = form.cleaned_data.get("description")
            photo = form.cleaned_data.get("photo")
            print(form.cleaned_data)
            return HttpResponse('yes')
        return render(request, 'index.html', {'form': Registration})
