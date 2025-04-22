from django import forms
from django.contrib.auth.models import User
from .models import UserAddress

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите адрес электронной почты',
            }),
        }
        
from django import forms
from .models import UserAddress
        
class AddressForm(forms.ModelForm):
    class Meta:
        model = UserAddress
        fields = ['street', 'city', 'state', 'postal_code', 'country', 'contact_name', 'phone_number']