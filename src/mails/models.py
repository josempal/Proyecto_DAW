# Django
from django.db import models
# App
from accounts.models import User

class Mail(models.Model):

    subject = models.CharField(max_length=50)
    body = models.CharField(max_length=500, null=True)
    is_read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    from_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='mails_sent')
    to_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='mails_received')
    parent_message = models.ForeignKey('self', null=True, on_delete=models.DO_NOTHING, related_name='mails_child')
