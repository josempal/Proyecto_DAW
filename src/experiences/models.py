from django.db import models
from accounts.models import Profile

class Experience(models.Model):

    TYPE = (
        ('CURSO', 'Curso'),
        ('PROFESIONAL', 'Profesional'),
        ('ARTISTICA', 'Artistica'),
        ('OTRO', 'Otro')
    )

    DURATION = (
        ('0-3', '0 a 3 meses'),
        ('3-6', '3 a 6 meses'),
        ('6-1A', '6 meses a 1 año'),
        ('1A-2A', '1 año a 2 años'),
        ('2A-4A', '2 años a 4 años'),
        ('4A-6A', '4 años a 6 años'),
        ('6+', '6 años o mas')
    )

    center = models.CharField(max_length=200, null=True, blank=True)
    group = models.CharField(max_length=200, null=True, blank=True)
    type = models.CharField(max_length=50, choices=TYPE)
    duration = models.CharField(max_length=50, choices=DURATION)
    observations = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name='experiences')

    class Meta:

        ordering = ('-updated',)