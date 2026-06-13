import re

from django import forms
from django.core.exceptions import ValidationError

from .models import Order


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order

        fields = [
            'full_name',
            'mobile_number',
            'address_line',
            'city',
            'postal_code',
            'quantity',
        ]

        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Full Name'
            }),

            'mobile_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '03XXXXXXXXX'
            }),

            'address_line': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Street Address'
            }),

            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'City'
            }),

            'postal_code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Postal Code'
            }),

            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1
            }),
        }

    def clean_mobile_number(self):

        mobile = self.cleaned_data.get('mobile_number')

        mobile = mobile.strip()

        if not re.match(r'^\d{10,11}$', mobile):
            raise ValidationError(
                "Mobile number must contain 10–11 digits."
            )

        return mobile

    def clean_full_name(self):

        full_name = self.cleaned_data.get('full_name')

        if len(full_name.strip()) < 3:
            raise ValidationError(
                "Please enter a valid full name."
            )

        return full_name

    def clean_address_line(self):

        address = self.cleaned_data.get('address_line')

        if len(address.strip()) < 5:
            raise ValidationError(
                "Please enter a complete address."
            )

        return address

    def clean_city(self):

        city = self.cleaned_data.get('city')

        if len(city.strip()) < 2:
            raise ValidationError(
                "Please enter a valid city."
            )

        return city