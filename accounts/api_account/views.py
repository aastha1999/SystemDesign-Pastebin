from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse


# from paste.models import Account, PasteFile
from accounts.api_account.serializers import RegisterSerializers

from rest_framework.authtoken.models import Token
from accounts.models import User
from django.contrib.auth import get_user_model 


@api_view(['POST'])
def registration_view(request):    
    if request.method == 'POST':
        # data1 = json.loads(request.data)
        email = request.data.get("email")
        username = request.data.get("username")
        # email, username = data1['email'], data1['username']
        account = User.objects.filter(email=email).first()
        account1 = User.objects.filter(username=username).first()

        if(account!=None):
            response = json.dumps({'Error': "Email already exists"})
            return HttpResponse(response, content_type='application/json')

        if(account1!=None):
            response = json.dumps({'Error': "Username already exists"})
            return HttpResponse(response, content_type='application/json')     
        serializer = RegisterSerializers(data = request.data)
        data = {}
        if serializer.is_valid():
           account = serializer.save() 
           data['response'] = "succefully registered a new user."
           data['email'] = account.email
           data['username'] = account.username
        
        else:
            data = serializer.errors

        return Response(data)    
