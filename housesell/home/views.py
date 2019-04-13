from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import ListView

from home.models import Enquiry
from property.models import Property
from .forms import EnquiryForm


class Base(ListView):
    model = Property
    template_name = 'base.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Base, self).get_context_data(**kwargs)
        context['property'] = Property.objects.filter(property_is_published=True).order_by('-property_listing_date')[:3]
        return context


def property_listings(request):
    property_list = Property.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(property_list, 3)
    try:
        property = paginator.page(page)
    except PageNotAnInteger:
        property = paginator.page(1)
    except EmptyPage:
        property = paginator.page(paginator.num_pages)

    return render(request, 'property_list.html', {'property_all': property})


def search_property(request):
    if request.method == 'POST':
        title = request.POST.get('search')
        city = request.POST.get('city')
        states = request.POST.get('state')
        try:

            if title != '':
                if city != 'City':
                    if states != 'State':
                        query = Q(property_title__contains=title) & Q(property_city__contains=city) & Q(
                            property_states__contains=states)
                        print('1')
                    else:
                        query = Q(property_title__contains=title) & Q(property_city__contains=city)
                        print('2')
                else:
                    if states != 'State':
                        query = Q(property_title__contains=title) & Q(property_states__contains=states)
                        print('3')
                    else:
                        query = Q(property_title__contains=title)
                        print('4')
            else:
                if city != 'City':
                    if states != 'State':
                        query = Q(property_city__contains=city) & Q(property_states__contains=states)
                        print('5')
                    else:
                        query = Q(property_city__contains=city)
                        print('6')
                else:
                    if states != 'State':
                        query = Q(property_states__contains=states)
                        print('7')
                    else:
                        query = Q(property_title__contains=title) | Q(property_city__contains=city) | Q(
                            property_states__contains=states)
                        print('8')

            result = Property.objects.filter(query)

            if result:
                messages.success(request, 'Property Found Successfully')
                return render(request, 'success_page.html', {'property': result, 'n_o_p': len(result) - 1})
            else:
                messages.error(request, 'No Property Found !')
                return render(request, 'success_page.html', {'n_o_p': 0})

        except Property.DoesNotExist:
            return HttpResponse("<h1>Property Does Not Exist</h1>")

    else:
        return redirect('home:base')


@login_required
def enquire_property(request, id):
    if request.method == "POST" and not request.user.is_seller:
        enquire_form = EnquiryForm(request.POST)
        if enquire_form.is_valid():
            try:
                property_obj = Property.objects.get(id=id)
            except Property.DoesNotExist:
                return HttpResponse("<h1>The property you are trying to access does not exist</h1>")

            try:
                Enquiry.objects.get(person=request.user, property=property_obj)
                messages.error(request, "Sorry You have already enquired about this property")
            except Enquiry.DoesNotExist:
                enquire_form.instance.property_id = id
                enquire_form.instance.person_id = request.user.id
                enquire_form.save()
                messages.success(request, "The enquiry Posted successfully ")
        else:
            enquire_form = EnquiryForm()

        return render(request, 'enquiry_result.html', {'form': enquire_form, 'prop': property_obj})
    else:
        try:
            property_obj = Property.objects.get(id=id)
        except Property.DoesNotExist:
            return HttpResponse("<h1>The property you are trying to access does not exist</h1>")

        if request.user.is_seller:
            return HttpResponse("<h1>You need to be buyer to post the enquiry !!")
        enquire_form = EnquiryForm()
        return render(request, 'enquiry_result.html', {'form': enquire_form, 'prop': property_obj})






