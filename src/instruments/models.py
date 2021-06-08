from django.db import models
from accounts.models import Profile

class Instrument(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, null=True, blank=True)
    instrumentalists = models.ManyToManyField(Profile, through='InstrumentUser', related_name='instruments', db_table='instrument_user'),
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) 

class IntrumentUser(models.Model):

    LEVELS = (
        ('PRINCIPIANTE', 'Principiante'),
        ('ELEMENTAL', 'Grado elemental'),
        ('MEDIO', 'Grado medio'),
        ('SUPERIOR', 'Grado superior'),
        ('ELEMENTAL-NO', 'Grado elemental (sin titulación)'),
        ('MEDIO-NO', 'Grado medio (sin titulación)'),
        ('SUPERIOR-NO', 'Grado superior (sin titulación)'),
        ('MASTER', 'Máster')
    )

    profile = models.ForeignKey(Profile)
    instrument = models.ForeignKey(Instrument)
    level = models.CharField(max_length=50, choices=LEVELS)