from rest_framework import serializers
from . import models
from .models import Admin, Client


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        exclude = ['password']


class AdminSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = models.User
        fields = ['username', 'first_name', 'last_name','email', 'password', 'password2']

    def save(self, **kwargs):
        user = models.User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error': 'password do not match'})
        user.set_password(password)
        user.is_staff = True
        user.save()
        models.Admin.objects.create(user=user)
        return user


class ClientSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = models.User
        fields = ['username', 'email', 'password', 'password2']
        # extra_kwargs = {
        #     'password':{'write_only':True}
        # }

    def save(self, **kwargs):
        user = models.User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
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