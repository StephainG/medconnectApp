# Generated by Django 4.2.1 on 2023-06-21 12:42

from django.db import migrations, models
import medconnectApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('medconnectApp', '0008_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='default/logo.jpg', upload_to=medconnectApp.models.User.image_upload_to),
        ),
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('REGULAR', 'REGULAR'), ('GOLD', 'GOLD'), ('PLATINUM', 'PLATINUM')], default='REGULAR', max_length=255),
        ),
    ]
