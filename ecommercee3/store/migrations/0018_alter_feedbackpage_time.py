# Generated by Django 5.0.3 on 2024-04-19 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_feedbackpage_alter_contactpage_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackpage',
            name='Time',
            field=models.DateTimeField(),
        ),
    ]
