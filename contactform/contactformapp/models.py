from django.db import models

# Create your models here.
class contactform(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.BigIntegerField() 
    company = models.CharField(max_length=100)
    salary = models.IntegerField()
    location= models.CharField(max_length=100)

     