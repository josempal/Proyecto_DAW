# Django
from django.db import models
from django.urls import reverse
# App
from accounts.models import User

class Mail(models.Model):

    subject = models.CharField(max_length=50)
    body = models.CharField(max_length=500, null=True, blank=True)
    is_read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    from_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='mails_sent')
    to_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='mails_received')
    parent_message = models.ForeignKey('self', on_delete=models.DO_NOTHING, related_name='mails_child', null=True, blank=True)

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
	    return reverse('mails:mail-detail', kwargs={'pk': self.id})

    def readable_date(self):
        return self.created.strftime("%a %d %B %y")