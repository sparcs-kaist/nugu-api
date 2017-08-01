from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.api.serializers import UserSerializer, UserPublicSerializer
from .models import User

@api_view(['GET'])
def user_list(request):
    users = User.objects.all().order_by('-ent_year')
    serializer = UserPublicSerializer(users, many=True)
    return Response(serializer.data)

@login_required
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    """
    Retrieve, update or delete an user instance.
    """

    if request.method in ['GET', 'DELETE']:
        try:
            user = User.objects.get(id=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        try:
            user = User.objects.get(id=pk)
        except User.DoesNotExist:
            user = User()

        data = request.data
        data["id"] = pk

        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
