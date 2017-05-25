from rest_framework import viewsets
from apps.api.serializers import UserSerializer
from .core import nugu_list
from .models import create_session, User

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    session = create_session()
    queryset = nugu_list(session)

    # queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

