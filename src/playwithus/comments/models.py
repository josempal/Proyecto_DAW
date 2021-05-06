from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    
    body = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='comments_sent')
    receiver = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='comments_received')

    class Meta:

        ordering = ('-updated',)