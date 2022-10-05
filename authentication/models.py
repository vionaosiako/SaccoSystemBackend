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
    othername = models.CharField(max_length=100,blank=True,null=True)
    gender = models.CharField(max_length=15,blank=True,null=True)
    residential_area = models.CharField(max_length=100,blank=True,null=True)
    national_id = models.CharField(max_length=15,blank=True,null=True)
    date_of_birth = models.DateField(blank=True,null=True)
    phone_number = models.CharField(max_length=15,blank=True,null=True)

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

class NextOfKin(models.Model):
    surname = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    othername = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    national_id = models.IntegerField(blank=True, null=True)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    percentage = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='nextofkin')
    
    def __str__(self):
        return self.surname
