from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .models import UserAccount
from .serializers import *

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserDetailSerializer

    @action(detail=True)
    def user_get(self, request, *args, **kwargs):
        User = get_user_model()
        self.object = get_object_or_404(User, pk=kwargs["pk"])
        serializer = self.get_serializer(self.object)
        return Response(serializer.data)

    @action(detail=True)
    def user_me(self, request):
        if request.user.is_authenticated:
            serializer = self.get_serializer(request.user)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    @action(permission_classes=(IsAuthenticated,), detail=True)
    def user_edit_get(self, request, *args, **kwargs):
        User = get_user_model()
        self.object = get_object_or_404(User, pk=kwargs["pk"])
        serializer = UserEditSerializer(self.object)
        return Response(serializer.data)

    @action(permission_classes=(IsAuthenticated,), detail=True)
    def user_edit_post(self, request, *args, **kwargs):
        if request.user.id and kwargs['pk'] == request.user.id:
            data = request.data
            serializer = self.serializer_class(data=data, partial=True)
            if serializer.is_valid():
                serializer.update(instance=request.user, validated_data=data)
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)




