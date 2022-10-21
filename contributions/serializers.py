from rest_framework import serializers
from . import models
from .models import MonthlyContribution,MerryGoRoundContribution

class MonthlyContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MonthlyContribution
        fields = '__all__'
        
class MerryGoRoundContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MerryGoRoundContribution
        fields = '__all__'