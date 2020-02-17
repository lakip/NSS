from django import forms


class Register(forms.Form):
    admno = forms.IntegerField(required=True)
    first_name = forms.CharField()
    last_name = forms.CharField()
    address = forms.IntegerField()
    town = forms.CharField()
    county = forms.CharField()
    postal_code = forms.IntegerField()
    # next of kin
    fname = forms.CharField()
    lname = forms.CharField()
    phone = forms.IntegerField()


