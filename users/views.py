from rest_framework import APIView
from rest_framework.response import Response
from rest_framework import status,permissions
from django.contrib.auth import get_user_model
User=get_user_model()

from .serializers import UserCreateSerializer
# Create your views here.
class RegisterView(APIView):
    def post(self,request):
        data=request.data
        first_name=data['first_name']
        last_name=data['last_name']
        email=data['email']
        password=data['password']

        user=User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
            )
        user=UserCreateSerializer(user)
        return Response(user.data, status=status.HTTP_201_CREATED)


class RetrieveUserView(APIView):
    def get(self, request):
        print(request.user)
        return Response(status=status.HTTP_200_OK)
    