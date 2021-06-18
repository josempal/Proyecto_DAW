# Django
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.conf import settings
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
# 3rd party
from autoslug import AutoSlugField

class UserManager(BaseUserManager):
	"""Define a model manager for User model with no username field."""

	use_in_migrations = True

	def _create_user(self, email, password, **extra_fields):
		"""
        Create and save a User with the given email and password
        """
		if not email:
			raise ValueError('The given email must be set')
		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, email, password=None, **extra_fields):
		"""
        Create and save a regular User with the given email and password
        """
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(email, password, **extra_fields)

	def create_superuser(self, email, password, **extra_fields):
		"""
        Create and save a SuperUser with the given email and password
        """
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have is_staff=True.')
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')

		return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """
    User model with email as username
    """
    username = None
    first_name= models.CharField(null=True, blank=True, max_length=100)
    last_name = models.CharField(null=True, blank=True, max_length=100)
    email = models.EmailField(_('email address'), unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    is_group = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager() 
    
    def __str__(self):
        return self.email
        
class Profile(models.Model):
    """
    Proxy model that extends the base data with other information.
    """
    displayname = models.CharField(max_length=150, unique=True)
    bio = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='avatars/', default='avatars/no_avatar.png', blank=True)
    location = models.CharField(max_length=25, blank=True, null=True)
    is_public = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='profile')
    slug = AutoSlugField(populate_from='displayname', unique=True)

    def __str__(self):
        return self.displayname

    def get_absolute_url(self):
	    return reverse('accounts:profile-detail', kwargs={'slug': self.slug})

def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:    
        try:
            # Populate displayname with email's username part
            dn_from_email = instance.email.split('@')
            Profile.objects.create(user=instance, displayname=dn_from_email[0])
        except:
            pass

post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)
