# Generated by Django 3.0.3 on 2020-02-21 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20200221_1042'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentregister',
            old_name='form',
            new_name='formclass',
        ),
    ]
