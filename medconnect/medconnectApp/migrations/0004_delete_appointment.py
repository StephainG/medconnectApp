# Generated by Django 4.2.1 on 2023-06-06 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medconnectApp', '0003_rename_name_user_first_name_user_last_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Appointment',
        ),
    ]