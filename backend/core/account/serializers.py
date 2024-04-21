from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UserAccount
from collection.models import UserCollection
from collection.serializers import UserCollectionSerializer

User = get_user_model()


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
    collections = serializers.SerializerMethodField()
    class Meta(UserSerializer.Meta):
        model = User
        fields = ('id',
                  'email',
                  'first_name',
                  'last_name',
                  'phone',
                  'collections',
                  )
    def get_collections(self, user):
        user_collections = UserCollection.objects.filter(user=user)

        collection_serializer = UserCollectionSerializer(user_collections, many=True)
        return collection_serializer.data

class UserEditSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = ('first_name',
                  'last_name',
                  'email',
                  'phone',
                  'id',
                  )