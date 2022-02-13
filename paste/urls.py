from django.urls import path
from django.conf.urls import include

from .views import  CreateNewPaste, Detail, Index,  RawContent, GetUrl, find_url, GetRawPaste, deleteUrl, AllPastes,GetUser,GetToken
from paste.api.views import api_detail_paste_view

from accounts.api_account.views import registration_view

from rest_framework.authtoken.views import obtain_auth_token
# from .views import  Detail, Index,  RawContent, GetUrl, find_url, GetRawPaste

app_name = "paste"

urlpatterns = [
    # homepage
    path("", Index.as_view(), name="index"),


    ## API calls

    path('api/account/register/', registration_view, name='register'),


    # get slug details
    # input: slug
    path('<str:slug>/', Detail.as_view(), name='detail'),


    # get raw content of slug
    # input: slug
    # output: PasteFile contents
    path('api/raw/<str:slug>/', RawContent.as_view(), name='raw_content'),


    # create URL
    # input: content and title
    # output: slug
    # logic: if title & content already exists, return existing slug, else return new slug
    path('api/createURL/', GetUrl.as_view(), name='create_url'),


    # create URL
    # input: title, content
    # output: slug
    path('api/create/', CreateNewPaste.as_view(), name='create'),


    # delete an existing slug
    # input: slug
    path('api/delete/', deleteUrl.as_view(), name='delete'),


    # get contents of an existing slug
    # input: slug
    # output: PasteFile contents
    path('api/get_content/', GetRawPaste.as_view(), name='get_content'),


    # get token of an existing user
    # input: 
    # output: token ID
    path('api/getToken/', GetToken.as_view(), name='get_user'),

    
    # get user details
    # input: 
    # output: 
    path('api/getUser/', GetUser.as_view(), name='get_user'),


    # get all pastes from the database
    path('api/allpastes/', AllPastes.as_view(), name='all_pastes')
]
