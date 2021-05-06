from django.db import models
from django.contrib.auth.models import User

class Mail(models.Model):

    subject = models.CharField(max_length=50)
    body = models.CharField(max_length=500, null=True)
    created = models.DateTimeField(auto_now_add=True)
    from_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='mails_sent')
    to_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='mails_received')
    parent_message = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='mails_child')
