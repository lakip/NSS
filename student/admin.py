# -*- encoding: utf-8 -*-

from django.contrib import admin
from .models import StudentRegister


class StudentAdmin(admin.ModelAdmin):
    fields = ['admno', 'first_name', 'last_name']


admin.site.register(StudentRegister, StudentAdmin)
