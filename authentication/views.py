from django.shortcuts import render
from rest_framework import generics

from utils.paginator import CustomPaginator
from .serializers import ClientSerializer, UserSerializer, AdminSerializer
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser # image upload
from rest_framework import viewsets
from . import models

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/users',
        'api/admin',
        'api/client',
        'api/token',
        'api/token/refresh/',
    ]
    return Response(routes)


class AdminSignUpView(generics.GenericAPIView):
    serializer_class = AdminSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data) #request data from the database before posting checks if  data is unique
        serializer.is_valid(raise_exception=True)#validates the data
        user = serializer.save()#save the new user if everything is correct
        context = {
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'token': Token.objects.get(user=user).key,
            'message': 'Account made successfully' #return the message
        }
        return Response(context)


class ClientSignUpView(generics.GenericAPIView):
    serializer_class = ClientSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        context = {
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'token': Token.objects.get(user=user).key,
            'message': 'Account made successfully'
        }
        return Response(context)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    pagination_class = CustomPaginator  # Use your custom paginator

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            page = self.paginate_queryset(queryset)

            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.paginator.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({
                'status': False,
                'message': 'Error retrieving users',
                "error": str(e)
            })

