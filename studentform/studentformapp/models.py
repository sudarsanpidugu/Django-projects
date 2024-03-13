from django.db import models

# Create your models here.
class studentdata(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.BigIntegerField()
    college = models.CharField(max_length=100)
    qulification = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    percentage = models.IntegerField()
    fee = models.IntegerField()
