from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
# from cloudinary.models import CloudinaryField


# Create your models here.
class User(AbstractUser):
    is_staff = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)

    def __str__(self):
        return str(self.username)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Admin(models.Model):
    user = models.OneToOneField(User, related_name='admins', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username)


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client')

    def __str__(self):
        return str(self.user.username)
