# Generated by Django 2.0.6 on 2018-07-16 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subby', '0010_auto_20180715_2246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sublet',
            name='front_image',
        ),
    ]