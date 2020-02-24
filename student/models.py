from django.db import models

clss = [
    ('Form1', 'Form One'),
    ('Form2', 'Form Two'),
    ('Form3', 'Form Three'),
    ('Form4', 'Form Four'),
]


class StudentRegister(models.Model):
    admno = models.IntegerField(default=1, primary_key=True)
    formclass = models.CharField(max_length=20, default='', choices=clss)
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    address = models.IntegerField(default=00)
    town = models.CharField(max_length=50, default='')
    county = models.CharField(max_length=50, default='')
    postal_code = models.IntegerField(default=0000)
    # next of kin
    fname = models.CharField(max_length=50, default='')
    lname = models.CharField(max_length=50, default='')
    phone = models.IntegerField(default=1234567)

    def __str__(self):
        return self.formclass

    def get_absolute_url(self):
        return 'register_student/'

    class Meta:
        db_table = 'StudentRegister'


