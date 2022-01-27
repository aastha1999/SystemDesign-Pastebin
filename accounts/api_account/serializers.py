# from re import I
from rest_framework import serializers
from accounts.models import User
from django.contrib.auth.hashers import make_password

class RegisterSerializers(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email','username','password','password2']
        extra_kwargs = {
            'password':{'write_only': True}
        }

    def save(self):
        pastefile = User(
            email = self.validated_data['email'],
            username=self.validated_data['username'],
        )  
        password = self.validated_data['password'] 
        password2 = self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwods must match.'})
        pastefile.password = make_password(password)
        pastefile.save()    
        return pastefile