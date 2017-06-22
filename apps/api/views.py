from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from apps.api.serializers import UserSerializer
# from .core import nugu_list
from .models import User


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by('-ent_year')
    serializer_class = UserSerializer

    @list_route()
    def all(self, request):
        all_users = User.objects.all().order_by('-ent_year')
        serializer = self.get_serializer(all_users, many=True)
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def get(self, request, pk=None):
        users = User.objects.filter(id=pk).first()
        serializer = self.get_serializer(users)
        return Response(serializer.data)
