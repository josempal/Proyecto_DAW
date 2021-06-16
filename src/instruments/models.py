from django.db import models
from accounts.models import Profile

class Instrument(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, null=True, blank=True)
    instrumentalists = models.ManyToManyField(Profile, through='InstrumentUser', related_name='instruments',)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name    

class InstrumentUser(models.Model):

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

    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING,)
    instrument = models.ForeignKey(Instrument,on_delete=models.DO_NOTHING,)
    level = models.CharField(max_length=50, choices=LEVELS)

    def __str__(self):
        return f"{self.profile.displayname} - {self.instrument.name} | {self.level}"