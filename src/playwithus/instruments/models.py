from django.db import models
from django.contrib.auth.models import User

class Instrument(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, null=True, blank=True)
    instrumentalists = models.ManyToManyField(User, related_name='instruments', db_table='instrument_user'),
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) 