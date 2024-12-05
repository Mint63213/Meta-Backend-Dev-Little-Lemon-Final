from django.forms import ModelForm
from django import forms
from .models import Booking
import bleach


# Code added for loading form data on the Booking page
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['first_name', 'last_name', 'guest_number', 'comment', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }   

    def clean(self):
        cleaned_data = super().clean()
        for field in cleaned_data:
            if field != 'guest_number' and field != 'date':
                cleaned_data[field] = bleach.clean(cleaned_data[field])
        return cleaned_data

