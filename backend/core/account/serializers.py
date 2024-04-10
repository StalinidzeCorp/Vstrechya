from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UserAccount

User = UserAccount

class UsersCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id',
                  'email',
                  'first_name',
                  'last_name',
                  'created_at',
                  'updated_at',
                  'phone',
                  )
class UserDetailSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = ('id',
                  'email',
                  'first_name',
                  'last_name',
                  )