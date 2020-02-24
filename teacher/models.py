from django.db import models


class TReacher(models.Model):
    tsc_no = models.IntegerField(primary_key=True)
    first_name = models.CharField(default='', max_length=50)
    last_name = models.CharField(default='', max_length=50)
    teaching_subjects = models.CharField(default='', max_length=50)
    teaching_subjects2 = models.CharField(default='', max_length=50)

    class Meta:
        db_table = 'TeacherRegister'


