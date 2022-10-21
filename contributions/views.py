from django.shortcuts import render
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser # image upload
from rest_framework import viewsets
from . import models

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
