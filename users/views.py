from users.models import Users
from users.serializers import UsersSerializer, UsersUpdateSerializer
from rest_framework import generics
#some more additions
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


class UsersList(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class UsersDetail(generics.RetrieveDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class UsersUpdate(generics.RetrieveUpdateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersUpdateSerializer

