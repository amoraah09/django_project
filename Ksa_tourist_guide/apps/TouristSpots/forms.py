from django import forms
from .models import TouristSpots

class TouristSpotsForm(forms.ModelForm):
    class Meta:
        model = TouristSpots
        fields = ['name', 'city', 'description', 'location']

    name = forms.CharField(
        max_length=100,
        required=True,
        label='Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter name'
            }
        )
    )
    city = forms.CharField(
        max_length=100,
        required=True,
        label='City',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter city'
            }
        )
    )
    description = forms.CharField(
        required=True,
        label='Description',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter description'
            }
        )
    )
    location = forms.CharField(
        max_length=200,
        required=True,
        label='Location',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter location'
            }
        )
    )
