from rest_framework import viewsets
from apps.api.serializers import UserSerializer
# from .core import nugu_list
from .models import User


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    print(User.objects.all())
    queryset = User.objects.all().order_by('-ent_year')
    serializer_class = UserSerializer
