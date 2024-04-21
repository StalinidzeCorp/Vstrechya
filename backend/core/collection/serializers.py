from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Collection

User = get_user_model()


class UserCollectionSerializer(UserCreateSerializer):
    class Meta:
        model = Collection
        fields = ('id','name')