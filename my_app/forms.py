from django import forms
from .models import Stop

class StopForm(forms.ModelForm):
    class Meta:
        model = Stop
        fields = ['name', 'date', 'rating']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }