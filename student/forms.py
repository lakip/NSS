from django import forms
from .models import StudentRegister


class StudentRegistration(forms.Form):
    admno = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Admission Number",
                "class": "form-control"
            }
        ))
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'First Name',
                'class': 'form-control',
            }
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter Second Name',
                'class': 'form-control',
            }
        )
    )
    address = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'address',
                'class': 'form-control',
            }
        )
    )
    town = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Town',
                'class': 'form-control',
            }
        )
    )
    county = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'County of Birth',
                'class': 'form-control'
            }
        )
    )
    postal_code = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter Postal code',
                'class': 'form-control'
            }
        )
    )
    fname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter  Parent/Guardian name',
                'class': 'form-control'
            }
        )
    )
    lname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter  Parent/Guardian name',
                'class': 'form-control'
            }
        )
    )
    phone = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter  Parent/Guardian Phone Number',
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = StudentRegister
        fields = ['admno', 'first_name', 'last_name', 'address', 'town', 'county', 'postal_code', 'fname', 'lname', 'phone']








