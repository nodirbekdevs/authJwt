from rest_framework.serializers import ModelSerializer, SerializerMethodField
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    name = SerializerMethodField(read_only=True)
    _id = SerializerMethodField(read_only=True)
    is_admin = SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'is_admin']

    def get__id(self, obj):
        return obj.id

    def get_is_admin(self, obj):
        return obj.is_staff

    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.email
        return name
