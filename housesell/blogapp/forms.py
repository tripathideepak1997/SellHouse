from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User
import re


class Registration(UserCreationForm):
    # email_id = forms.EmailField(max_length=50, required=True,
    #                             widget=forms.EmailInput(attrs={
    #                                 'class': 'wrap-input100 validate-input',
    #                                 'placeholder': 'Email Address'
    #                             }))
    # is_seller = forms.CheckboxInput()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email_id', 'phone', 'password1',
                  'password2', 'is_seller', 'description',
                  'photo', )

    def clean(self):
        cd = self.cleaned_data
        pattern_name = re.compile("/^[\w]*$")
        patter_number = re.compile("^(?:(?:\+|0{0,2})91(\s*[\ -]\s*)?|[0]?)?[789]\d{9}|(\d[ -]?){10}\d$")

        if not re.match(patter_number, str(cd.get("phone"))):
            self.add_error('phone', "The phone number must be in Indian Format +91 starting or with "
                                    "977587666,0 9754845789,0-9778545896,+91 9456211568,91 9857842356,"
                                    "919578965389,03595-259506,03592 245902")

        if not re.match(pattern_name, str(cd.get("first_name"))):
            self.add_error('first_name', "Provide first name  in proper format")

        if not re.match(pattern_name, str(cd.get("last_name"))):
            self.add_error('last_name', "Provide last name  in proper format")

        return cd
