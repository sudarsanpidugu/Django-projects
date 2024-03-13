# Generated by Django 5.0.3 on 2024-03-12 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employeeformdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('mobile', models.BigIntegerField()),
                ('qulification', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('percentage', models.IntegerField()),
                ('passed_out_year', models.IntegerField()),
                ('skills', models.CharField(max_length=100)),
            ],
        ),
    ]