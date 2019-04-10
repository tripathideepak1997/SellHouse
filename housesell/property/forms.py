from django import forms
from property.models import Property


class PropertyRegistration(forms.ModelForm):

    class Meta:
        model = Property
        fields = ('property_title', 'property_address',
                  'property_city', 'property_states', 'property_pin',
                  'property_pin', 'property_price', 'property_bedroom',
                  'property_bathroom', 'property_sq_feet', 'property_lot_size',
                  'property_garage','property_description', 'photo_main',
                  'photo1', 'photo2', 'photo3', 'photo4', 'photo5', 'photo6')


class PropertyUpdate(forms.ModelForm):
    class Meta:
        model = Property
        fields = ('property_title', 'property_address',
                  'property_city', 'property_states', 'property_pin',
                  'property_pin', 'property_price', 'property_bedroom',
                  'property_bathroom', 'property_sq_feet', 'property_lot_size',
                  'property_garage', 'property_description', 'photo_main',
                  'photo1', 'photo2', 'photo3', 'photo4', 'photo5', 'photo6')
