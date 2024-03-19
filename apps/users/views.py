from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .models import CustomUser
from .serializer import UserRegistrationSerializer, UserLoginSerializer


class UserRegistrationViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User registered successfully', 'user_id': user.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        queryset = CustomUser.objects.all()
        serializer = UserRegistrationSerializer(queryset, many=True)
        return Response(serializer.data)

class UserLoginViewSet(viewsets.ViewSet):

    def create(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
