# from django.shortcuts import render
# # from .serializers import MemberSerializer
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import permissions
# from rest_framework.parsers import MultiPartParser, FormParser, JSONParser # image upload
# from rest_framework import viewsets
# from . import models

# Create your views here.
# @api_view(['GET'])
# def getRoutes(request):
#     routes = [
#         'api/member',
#         'api/nextofkin',
#     ]
#     return Response(routes)

# class MemberViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = models.Member.objects.all()
#     serializer_class = MemberSerializer
    
# class MembersJointableapi(viewsets.ModelViewSet):
#     queryset=Jointablesmodel.objects.raw("select * from MemberJointtable inner join")

