# Generated by Django 5.0.3 on 2024-04-17 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_alter_otp_expiration_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='expiration_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]