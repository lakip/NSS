# Generated by Django 3.0.3 on 2020-02-12 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_termdates'),
    ]

    operations = [
        migrations.AddField(
            model_name='termdates',
            name='closing_day',
            field=models.DateField(default='2020-02-12'),
        ),
        migrations.AddField(
            model_name='termdates',
            name='opening_day',
            field=models.DateField(default='2020-02-12'),
        ),
    ]