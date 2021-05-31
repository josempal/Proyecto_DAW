# Django
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings
# 3rd party
from autoslug import AutoSlugField
class Profile(models.Model):
    """Profile model

    Proxy model that extends the base data with other information.
    """
    displayname = models.CharField(max_length=150, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='profiles/', default='profiles/no_avatar.png', blank=True)
    location = models.CharField(max_length=25, blank=True, null=True)
    is_public = models.BooleanField(default=True)
    slug = AutoSlugField(populate_from='displayname')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='profile')

    def __str__(self):
        return self.displayname

    def get_absolute_url(self):
	    return f"/profile/{self.slug}"

def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance, displayname=instance.username)
        except:
            pass

post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)