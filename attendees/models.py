from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Attendee(models.Model):
    full_name = models.CharField(max_length=70)
    phone_number = models.CharField(max_length=30)
    address = models.CharField(max_length=1000)
    church = models.CharField(max_length=1000)
    class Meta:
        db_table = 'attendee'

