from dj_rest_auth.views import LogoutView
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

import like.serializers
from . import serializers
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from like.serializers import FavoriteSerializer


class UserRegiseterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.RegisterSerializer


class CustomLogout(LogoutView):
    permission_classes = (permissions.IsAuthenticated,)


# class UserListView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = serializers.UserListSerializer
#     permission_classes = (permissions.IsAuthenticated,)
#
#
# class UserDetailView(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = serializers.UserDetailSerializers
#     permission_classes = (permissions.IsAuthenticated,)


class UserViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated, )

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.UserListSerializer()
        return serializers.UserDetailSerializers()

    @action(['GET'], detail=True)
    def favorites(self, request, pk):
        user = self.get_object()
        fav_post = user.favorites.all()
        serializer = like.serializers.FavoriteSerializer(fav_post, many=True)
        return Response(serializer.data, status=200)
