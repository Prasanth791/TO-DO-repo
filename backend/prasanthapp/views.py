from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

@api_view(['POST',])

def registration_view(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'Registration Successful'
            data['email'] = account.email
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)

@api_view(['POST'])

def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status= status.HTTP_200_OK)

@api_view(['GET'])
def getview(request):
    
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    return Response(queryset.values())
                        