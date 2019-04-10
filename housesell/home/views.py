from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import SearchForm
from property.models import Property


class Base(TemplateView):
    template_name = 'base.html'


def search_property(request):
    if request.method == 'POST':
        title = request.POST.get('search')
        city = request.POST.get('city')
        states = request.POST.get('state')
        try:
            status = Property.objects.filter(property_title__contains=title)
            status.union(Property.objects.filter(property_city__contains=city))
            status.union(Property.objects.filter(property_states__contains=states))
            if not status:
                messages.error(request, f'No Property Found !')
                return redirect('home:base')
            messages.success(request, 'Property Found Successfully')
            import pdb;
            pdb.set_trace()
            return render(request, 'success_page.html', {'property': status, 'n_o_p': len(status)-1})
        except Property.DoesNotExist:
            return HttpResponse("<h1>Property Does Not Exist</h1>")

    else:
        errors = "You are not requesting correctly"

    return render(request, 'base.html', {'errors': errors})
