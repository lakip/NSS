from django import forms
from .models import TReacher


subjects = [
    ('English', 'English'),
    ('Kiswahili', 'Kiswahili'),
    ('Mathematics', 'Mathematics'),
    ('Biology', 'Biology'),
    ('Chemistry', 'Chemistry'),
    ('Physics', 'Physics'),
    ('Geography', 'Geography'),
    ('History', 'History'),
    ('CRE', 'CRE'),
    ('Agriculture', 'Agriculture'),
    ('Business', 'Business Studies')
]


class Teacher(forms.Form):
    tsc_no = forms.IntegerField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    teaching_subjects = forms.CharField()
    teaching_subjects2 = forms.CharField()


class TeacherForm(forms.ModelForm):
    tsc_no = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter Tsc Number',
                'class': 'form-control col-md-12  pr-2 form-group'

            }
        )
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter Teacher`s first name',
                'class': 'form-control col-md-12  pr-2 form-group'

            }
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter Teachers last Number',
                'class': 'form-control col-md-12  pr-2 form-group'

            }
        )
    )
    teaching_subjects = forms.CharField(
        widget=forms.Select(
            attrs={
                'placeholder': 'Enter Teaching subjects',
                'class': 'form-control col-md-12  pr-2 form-group'
            },
            choices=subjects,
        )
    )
    teaching_subjects2 = forms.CharField(
        widget=forms.Select(
            attrs={
                'placeholder': 'Enter Teaching subjects',
                'class': 'form-control col-md-12  pr-2 form-group'
            },
            choices=subjects,
        )
    )

    class Meta:
        model = TReacher
        fields = ['tsc_no', 'first_name', 'last_name', 'teaching_subjects', 'teaching_subjects2']




