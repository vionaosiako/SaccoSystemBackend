from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.utils.crypto import get_random_string
# Create your models here.
STATUS =(
    ("Approved", "Approved"),
    ("Disapproved", "Disapproved"),
    ("Pending", "Pending"),
    )
LOANTYPE = (
        ('ElimuLoan','Elimu Loan'),
        ('AssetLoan', 'Asset Loan'),
        ('PersonalLoan', 'Personal Loan'),
    
    )
class LoanRequest(models.Model):
    id =models.CharField(max_length=6, primary_key = True, editable=False, unique=True)
    reg_number =  models.ForeignKey(User, on_delete=models.CASCADE)
    loan_type = models.TextField(choices=LOANTYPE,blank=False, default='Pending')
    amount_requested = models.IntegerField(default=0)
    status = models.TextField(choices=STATUS, blank=False, default='Pending')
    date_requested = models.DateField(auto_now_add=True,null=True,blank=True)
    
    def __str__(self):
        return self.reg_number.username
    
    class Meta:
        verbose_name = "Loan Request"
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = get_random_string(length=6, allowed_chars='123456')
        return super(LoanRequest, self).save(*args, **kwargs)
    
class LoanPayment(models.Model):
    payment_id = models.CharField(max_length=6, primary_key = True, editable=False, unique=True)
    loan_id =  models.ForeignKey(LoanRequest, on_delete=models.CASCADE)
    amount_paid = models.IntegerField(default=0)
    date_paid = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.loan_id.reg_number.username
    def save(self, *args, **kwargs):
        if not self.payment_id:
            self.payment_id = get_random_string(length=6, allowed_chars='123456')
        return super(LoanPayment, self).save(*args,**kwargs)