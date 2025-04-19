from django import forms
from django.contrib.auth.models import User

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        
from django import forms
from .models import UserAddress

class AddressForm(forms.ModelForm):
    class Meta:
        model = UserAddress
        fields = ['street', 'city', 'state', 'postal_code', 'country']