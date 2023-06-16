# Generated by Django 4.2.1 on 2023-06-09 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medconnectApp', '0004_delete_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('regular', 'regular'), ('gold', 'gold'), ('platinum', 'platinum')], default='regular', max_length=255),
        ),
    ]