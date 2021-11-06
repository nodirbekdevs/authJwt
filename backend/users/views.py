from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .serializers import UserSerializer


class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser, ]

    def create(self, request, *args, **kwargs):
        data = request.data
        try:
            user = User.objects.create(
                first_name=data['name'],
                username=data['username'],
                email=data['email'],
                password=make_password(data['password'])
            )
            serializer = UserSerializer(user, many=False)
            return Response(serializer.data)
        except:
            message = {'detail': 'User with this email already exists'}
            return Response(message, status=HTTP_400_BAD_REQUEST)