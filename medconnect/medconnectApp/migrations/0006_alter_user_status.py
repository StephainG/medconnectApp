# Generated by Django 4.2.1 on 2023-06-09 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medconnectApp', '0005_user_address_user_phone_number_user_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('regular', 'REGULAR'), ('gold', 'GOLD'), ('platinum', 'PLATINUM')], default='regular', max_length=255),
        ),
    ]