from django.db import models
from datetime import datetime

# Create your models here.


class Employees(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    date = models.DateTimeField(default=datetime.now, blank=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    company_role = models.CharField(max_length=50)


class Visitors(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    date = models.DateTimeField(default=datetime.now, blank=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    reason = models.CharField(max_length=50)
