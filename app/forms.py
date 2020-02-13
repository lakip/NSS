from django import forms
from django.contrib.auth.models import User


class Register(forms.Form):
    admno = forms.IntegerField()
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "First Name",
                "class": "form-control"
            }
        )
    )
    last_name = forms.CharField()
    address = forms.IntegerField()
    town = forms.CharField()
    county = forms.CharField()
    postal_code = forms.IntegerField()
    # next of kin
    fname = forms.CharField()
    lname = forms.CharField()
    phone = forms.IntegerField()

    class Meta:
        model = User
        fields = ('admno', 'first_name', 'last_name',
                  'address', 'town', 'county', 'postal_code', 'fname',
                  'lname', 'phone')
