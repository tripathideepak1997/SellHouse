from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from .forms import PropertyRegistration, PropertyUpdate
from .models import Property


@login_required
def register_property(request):
    if request.method == "POST" and request.user.is_seller:
        property_form = PropertyRegistration(request.POST, request.FILES)
        if property_form.is_valid():
            property_form.instance.user = request.user
            property_form.instance.property_poster_id = request.user.id
            property_form.instance.save()
            messages.success(request, f'Property has been registered !')
            return redirect('blogapp:property_view')
    else:
        property_form = PropertyRegistration()
        if not request.user.is_seller:
            return HttpResponse("<h1>You need to be seller to access this page</h1>")

    context = {'form': property_form, 'errors': property_form.errors}
    return render(request, 'property_register.html', context)


@login_required
def register_update(request, id):
    try:
        property = Property.objects.get(id=id)
    except Property.DoesNotExist:
        return HttpResponse("<h1>Id does not exist</h1>")

    if request.method == "POST" and request.user.is_seller:
        update_form = PropertyUpdate(request.POST, request.FILES, instance=property)
        if update_form.is_valid():
            update_form.save()
            messages.success(request, f'Register has been updated !')
            return redirect('property:property_view')
    else:
        update_form = PropertyUpdate(instance=property)
        if not request.user.is_seller:
            return HttpResponse("<h1>You need to be seller to access this page</h1>")
    context = {'u_form': update_form}
    return render(request, 'property_update.html', context)


@login_required
def property_view(request):
    errors = ""
    if request.user.is_seller and request.method == "GET":
        try:
            property = Property.objects.filter(property_poster=request.user)
        except Property.DoesNotExist:
            return HttpResponse("<h1>The current seller does not have any property</h1>")
        if len(property) != 0:
            return render(request, 'property_view.html',
                          {'property': property, 'n_o_p': len(property)-1, 'errors': errors})
        else:
            errors = "You don't have any property"

    else:
        errors = 'you are not requesting correctly'
        if not request.user.is_seller:
            return HttpResponse("<h1>You need to be seller to access this page</h1>")

    return render(request, 'property_view.html', {'errors': errors})


@login_required
def property_interiors(request, id):
    errors = ""
    if request.user.is_seller and request.method == "GET":
        try:
            property = Property.objects.get(id=id)
        except Property.DoesNotExist:
            return HttpResponse("<h1>Id does not exist</h1>")

        photo = ['photo1', 'photo2', 'photo3', 'photo4', 'photo5', 'photo6', ]

        interior_images = [getattr(property, photos) for photos in photo if getattr(property, photos)]
        if len(interior_images) != 0:
            return render(request, 'property_interior.html', {'property': property, 'n_o_p': len(interior_images)-1,
                                                              'interior': interior_images, 'errors': errors})
        else:
            errors = "You don't have interior images in this house"
    else:
        errors = "You need to be seller to view the page or you are not requesting correctly"

    return render(request, 'property_interior.html', {'errors': errors})
