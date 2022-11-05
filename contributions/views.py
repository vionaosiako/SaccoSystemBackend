from django.shortcuts import render
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser # image upload
from rest_framework import viewsets
from . import models
from authentication.models import User

# Create your views here.

class MonthlyContributionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.MonthlyContribution.objects.all()
    serializer_class = MonthlyContributionSerializer
    
class MerryGoRoundContributionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.MerryGoRoundContribution.objects.all()
    serializer_class = MerryGoRoundContributionSerializer

# class AccountViewSet(viewsets.ModelViewSet):
#     """
#     A simple ViewSet for viewing and editing the accounts
#     associated with the user.
#     """
#     serializer_class = AccountSerializer
#     permission_classes = [IsAccountAdminOrReadOnly]

#     def get_queryset(self):
#         return self.request.user.accounts.all()

@api_view(['GET','POST'])
def getMonthlyContribution(request):
    users=MonthlyContribution.objects.all()    
    serializedData=MonthlyContributionSerializer(instance=users, many=True)
    
    for value in serializedData.data:
        user=User.objects.filter(id=value['reg_number']).first()
        # print(user)
        value['first_name']=user.first_name
        value['last_name']=user.last_name

    return Response(serializedData.data)