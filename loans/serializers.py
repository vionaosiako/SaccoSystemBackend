from rest_framework import serializers
from . import models
from .models import *

class LoanCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LoanCategory
        fields = '__all__'

class LoanRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LoanRequest
        fields = '__all__'

class LoanPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LoanPayment
        fields = '__all__'