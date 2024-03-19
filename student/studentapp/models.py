from django.db import models

# Create your models here.
class studentdata(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.BigIntegerField()
    course_name = models.CharField(max_length=100)
    fee = models.IntegerField()
    institute_name = models.CharField(max_length=100)
    hometown = models.CharField(max_length=100)
    qulification = models.CharField(max_length=100)
    percentage = models.IntegerField()

