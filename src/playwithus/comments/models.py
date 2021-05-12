from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    
    body = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.PROTECT, related_name='comments_sent')
    profile = models.ForeignKey('users.Profile', on_delete=models.PROTECT, related_name='comments_received')

    class Meta:

        ordering = ('-updated',)