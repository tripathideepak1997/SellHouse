from django import forms

from property.models import Property


class SearchForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ('property_title','property_city', 'property_states', )
