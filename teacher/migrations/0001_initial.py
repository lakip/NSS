# Generated by Django 3.0.3 on 2020-02-23 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TReacher',
            fields=[
                ('tsc_no', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('teaching_subjects', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
