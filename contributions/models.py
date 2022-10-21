from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

#Create your models here.
class MonthlyContribution(models.Model):
    receipt_ID = models.AutoField(primary_key=True)
    reg_number =  models.ForeignKey(User, on_delete=models.CASCADE)
    Amount = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.reg_number)