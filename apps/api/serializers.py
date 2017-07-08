from .models import NUGU_FIELD_NAMES, User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id',) + tuple(NUGU_FIELD_NAMES)
