from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UserAccount
from collection.models import UserCollection, Collection
from collection.serializers import UserCollectionSerializer

User = get_user_model()


class UsersCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id',
                  'email',
                  'first_name',
                  'last_name',
                  'image_url',
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
                  'image_url',
                  'phone',
                  'collections',
                  )

    def get_collections(self, user):
        user_collections = UserCollection.objects.filter(user=user)
        collections = []
        for coll in user_collections:
            collections.append(UserCollectionSerializer(Collection.objects.get(id=coll.collection.id)).data)
        return collections


class UserEditSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = ('first_name',
                  'last_name',
                  'email',
                  'phone',
                  'image_url',
                  'id',
                  )
