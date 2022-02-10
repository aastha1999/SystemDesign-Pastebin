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
    path('api/get_content/', api_detail_paste_view, name='get_content'),
    path('api/account/register/', registration_view, name='register'),
    path('api/account/login/', registration_view, name='login'),
    # path('api/get_content/',include('paste.api.urls','paste_api')),


    # get slug details
    # input: slug
    path('<str:slug>/', Detail.as_view(), name='detail'),


    # get raw content of slug
    # input: slug
    # output: PasteFile contents
    path('raw/<str:slug>/', RawContent.as_view(), name='raw_content'),


    # create URL
    # input: content and title
    # output: slug
    # logic: if title & content already exists, return existing slug, else return new slug
    path('p/createURL/', GetUrl.as_view(), name='create_url'),


    # create URL
    # input: title, content
    # output: slug
    path('p/create/', CreateNewPaste.as_view(), name='create'),


    # delete an existing slug
    # input: slug
    path('p/delete/', deleteUrl.as_view(), name='delete'),


    # get contents of an existing slug
    # input: slug
    # output: PasteFile contents
    path('p/get_content/', GetRawPaste.as_view(), name='get_content'),


    # get token of an existing user
    # input: 
    # output: token ID
    path('p/getToken/', GetToken.as_view(), name='get_user'),

    
    # get user details
    # input: 
    # output: 
    path('p/getUser/', GetUser.as_view(), name='get_user'),


    # get all pastes from the database
    path('p/allpastes/', AllPastes.as_view(), name='all_pastes')
]
