from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """Profile model.

    Proxy model that extends the base data with other
    information.
    """
    displayname = models.CharField(max_length=150, blank=True, null=True)
    photo = models.ImageField(upload_to='users/pictures', blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT)