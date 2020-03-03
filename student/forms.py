from django import forms

from .models import StudentRegister

clss = [
    ('Form1', 'Form One'),
    ('Form2', 'Form Two'),
    ('Form3', 'Form Three'),
    ('Form4', 'Form Four'),

]


class StudentRegistration(forms.Form):
    admno = forms.IntegerField()
    formclass = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    address = forms.IntegerField()
    town = forms.CharField()
    county = forms.CharField()
    postal_code = forms.IntegerField()
    fname = forms.CharField()
    lname = forms.CharField()
    phone = forms.IntegerField()


class StudentForm(forms.ModelForm):
    admno = forms.IntegerField(
        label='Admission',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control col-md-12  pr-2 form-group ',
                'placeholder': 'Enter Admission Number',
            }
        )
    )
    formclass = forms.CharField(
        label='Form',
        widget=forms.Select(
            attrs={

                'class': 'form-control col-md-12 form-group ',
                'placeholder': 'Enter Form'
            },
            choices=clss
        )
    )
    first_name = forms.CharField(
        label='First Name',
        widget=forms.TextInput(
            attrs={

                'class': 'form-control col-md-12 pr-1',
                'placeholder': 'Enter Student`s First Name'

            }
        )
    )
    last_name = forms.CharField(
        label='Last Name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter Student`s last name',
                'class': 'form-control col-md-12 pr-1'
            }
        )
    )
    address = forms.IntegerField(
        label='Address',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control col-md-12 pr-1',
                'placeholder': 'Enter address'
            }
        )
    )
    town = forms.CharField(
        label='Town',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control col-md-12 pr-1',
                'placeholder': 'Enter Town',
            }
        )
    )
    county = forms.CharField(
        label='County',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control col-md-12 pr-1',
                'placeholder': 'Enter County',
            }
        )
    )
    postal_code = forms.IntegerField(
        label='Postal Code',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control col-md-12 pr-1',
                'placeholder': 'Postal code'
            }
        )
    )
    fname = forms.CharField(
        label='First Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control col-md-12 pr-1',
                'placeholder': 'Next of Kins first name'
            }
        )
    )
    lname = forms.CharField(
        label='Last Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control col-md-12 pr-1',
                'placeholder': 'Enter last name'
            }
        )
    )
    phone = forms.IntegerField(label='Phone Number',
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control col-md-12 pr-1',
                                       'placeholder': 'Enter phone Number'
                                   }
                               )
                               )

    class Meta:
        model = StudentRegister
        fields = ['admno', 'formclass', 'first_name', 'last_name', 'address', 'town', 'county', 'postal_code', 'fname',
                  'lname', 'phone']
