# from .models import UserModel
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):                                                                              
    mobileno = serializers.CharField(max_length = 30)
    conformpassword = serializers.CharField(style={'input-type':'password'}, write_only=True)
    
    class Meta:
        model = User
        fields =('username', 'first_name','last_name', 'mobileno','email', 'password','conformpassword' )
    
    def save(self):
        password = self.validated_data['password']
        conformpassword = self.validated_data['conformpassword']

        if password != conformpassword:
            raise serializers.ValidationError({'error':'password did not match'})

        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error':'email already exists'})

        account= User(username =self.validated_data['username'], first_name = self.validated_data['first_name'], last_name = self.validated_data['last_name'],email = self.validated_data['email'])

        account.set_password(password)
        account.save()
        return account

