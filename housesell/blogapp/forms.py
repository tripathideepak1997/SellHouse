from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


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

    def to_python(self):
        phone = self.cleaned_data.get("phone")
        if len(str(phone)) != 10:
            raise forms.ValidationError("Phone number must be of length 10")
        return phone
