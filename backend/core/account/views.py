import base64

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import UserAccount

from core.utils import upload_image
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserDetailSerializer

    def get_permissions(self):
        if self.action == 'user_edit_get' or self.action == 'user_edit_post' or self.action == 'upload_avatar':
            self.permission_classes = (IsAuthenticated,)
        else:
            self.permission_classes = (AllowAny,)
        return tuple(permission() for permission in self.permission_classes)

    @action(detail=True)
    def user_get(self, request, *args, **kwargs):
        User = get_user_model()
        self.object = get_object_or_404(User, pk=kwargs["pk"])
        serializer = self.get_serializer(self.object)
        return Response(serializer.data)

    @action(detail=True)
    def user_me(self, request):
        if request.user.is_authenticated:
            serializer = UserDetailSerializer(request.user)
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
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

    @action(permission_classes=(IsAuthenticated,), detail=True, methods=['post'])
    def upload_avatar(self, request, *args, **kwargs):
        img = request.data.get('img')
        if img:
            image_url = upload_image.delay(base64.b64encode(img.read()), 'avatars', True)
            user = request.user
            user.image_url = image_url.wait(timeout=None, interval=0.5)
            user.save()
            return Response({'image_url': user.image_url}, status=status.HTTP_200_OK)
        return Response({'img': 'no image'}, status=status.HTTP_400_BAD_REQUEST)

    # !ONLY FOR CHAT APP!
    @action(permission_classes=(IsAuthenticated,), detail=True)
    def all(self, request):
        serializer = UserCreateSerializer(User.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
