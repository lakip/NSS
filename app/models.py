# -*- encoding: utf-8 -*-
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

    class Meta:
        db_table = 'StudentRegister'


class TermDates(models.Model):
    opening_day = models.DateField(default='2020-02-12')
    closing_day = models.DateField(default='2020-02-12')

    class Meta:
        db_table = 'TermDates'


class Post(models.Model):
    title = models.CharField(max_length=300, unique=True)
    content = models.TextField()

    class Meta:
        db_table = 'Post'
