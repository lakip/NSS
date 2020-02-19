from django.db import models


class StudentRegister(models.Model):
    admno = models.IntegerField(default=1)
    first_name = models.CharField(max_length=50, default='first name')
    last_name = models.CharField(max_length=50, default='last name')
    address = models.IntegerField(default=00)
    town = models.CharField(max_length=50, default='town')
    county = models.CharField(max_length=50, default='county')
    postal_code = models.IntegerField(default=0000)
    # next of kin

    fname = models.CharField(max_length=50, default='fname')
    lname = models.CharField(max_length=50, default='last name')
    phone = models.IntegerField(default=1234567)

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return 'register_student/'

    class Meta:
        db_table = 'StudentRegister'

