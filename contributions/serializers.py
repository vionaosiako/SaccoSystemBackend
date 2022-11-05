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
        

def save(self, **kwargs):
        user = models.User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            othername=self.validated_data['othername'],
            gender=self.validated_data['gender'],
            phone_number=self.validated_data['phone_number'],
            residential_area=self.validated_data['residential_area'],
            national_id=self.validated_data['national_id'],
            date_of_birth=self.validated_data['date_of_birth'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error': 'password do not match'})
        user.set_password(password)
        user.is_client = True
        user.save()
        models.Client.objects.create(user=user)
        return user