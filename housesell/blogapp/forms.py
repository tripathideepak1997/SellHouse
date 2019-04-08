from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import User
import re


class Registration(UserCreationForm):
    # email_id = forms.EmailField(max_length=50, required=True,
    #                            )
    # is_seller = forms.CheckboxInput()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email_id', 'phone', 'password1',
                  'password2', 'is_seller', 'description',
                  'photo', )

    def clean(self):
        cd = self.cleaned_data
        patter_number = re.compile("^(?:(?:\+|0{0,2})91(\s*[\ -]\s*)?|[0]?)?[789]\d{9}|(\d[ -]?){10}\d$")

        if not re.match(patter_number, str(cd.get("phone"))):
            self.add_error('phone', "The phone number must be in Indian Format +91 starting or with "
                                    "977587666,0 9754845789,0-9778545896,+91 9456211568,91 9857842356,"
                                    "919578965389,03595-259506,03592 245902")
        return cd


class UserUpdateProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name',
                  'email_id', 'phone', 'description',
                  'photo', )

    def clean(self):
        cd = self.cleaned_data
        patter_number = re.compile("^(?:(?:\+|0{0,2})91(\s*[\ -]\s*)?|[0]?)?[789]\d{9}|(\d[ -]?){10}\d$")

        if not re.match(patter_number, str(cd.get("phone"))):
            self.add_error('phone', "The phone number must be in Indian Format +91 starting or with "
                                    "977587666,0 9754845789,0-9778545896,+91 9456211568,91 9857842356,"
                                    "919578965389,03595-259506,03592 245902")

        # email = self.cleaned_data.get("email_id")
        #
        # try:
        #     match = User.objects.get(email_id=email)
        # except User.DoesNotExist:
        #     User.objects['email_id'] = email
        #
        # self.add_error('email_id', "This email already exists Try different email")

        return cd

