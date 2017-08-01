from .models import NUGU_FIELD_NAMES, User
from rest_framework import serializers

class UserPublicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'is_developer', 'is_designer', 'github_id', 'linkedin_url', 'behance_url', 'website')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id',) + tuple(NUGU_FIELD_NAMES)
