from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Member(models.Model):
    othername = models.CharField(max_length=100)
    gender = models.CharField(max_length=15)
    residential_area = models.CharField(max_length=100)
    national_id = models.IntegerField()
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='member')
    
    def __str__(self):
        return self.user.username
    
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
    
# class Documents(models.Model):
    


