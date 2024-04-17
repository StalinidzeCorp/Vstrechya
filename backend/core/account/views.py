from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .models import UserAccount
from .serializers import *

User = UserAccount

# class testingAPI(APIView):
#     #permission_classes = [IsAuthenticated]
#     def get(self, request):
#         Users = User.objects.all()
#         serializer = UsersCreateSerializer(Users, many=True)
#
#         return Response(serializer.data)
#
#
# def test(request):
#     return HttpResponse('test page')
