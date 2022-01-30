from django.urls import path
from django.conf.urls import include

from .views import  CreateNewPaste, Detail, Index,  RawContent, GetUrl, find_url, GetRawPaste, deleteUrl, AllPastes,GetUser,GetToken
from paste.api.views import api_detail_paste_view

from accounts.api_account.views import registration_view

from rest_framework.authtoken.views import obtain_auth_token
# from .views import  Detail, Index,  RawContent, GetUrl, find_url, GetRawPaste

app_name = "paste"

urlpatterns = [
    # path("api/get_content/", api_detail_paste_view, name="get_content"),

    # Takes email, username and password as the input and will register that user in db if it diesn't exit already.
    path('api/account/register/', registration_view, name="register"),

    # path('api/account/login/', registration_view, name="login"),

    path("", Index.as_view(), name="index"),

    # returns title and content mapped with the given slug value in json format.
    path("<str:slug>/", Detail.as_view(), name="detail"),

    # path('api/get_content/',include('paste.api.urls','paste_api')),
    # path("get_url/<str:content>/<str:title>/",Detail.as_view(),name="Post"),
    # path("p/<str:title>/", get_url.as_view(), name="thread"),

    # returs raw content mapped with given slug value.
    path("raw/<str:slug>/", RawContent.as_view(), name="raw_content"),

    # path("find_url/<str:title>/<str:content>/", find_url.as_view(), name="url_link"),

    # path("shortenUrl", get_url.as_view(), name="get_url"),

    # To get the slug value. Input is the title and content. This also chceks like does the given content exist in db or not ? if yes then return the same slug value, otherwise create , store and then returns.
    path("p/shortenUrl/", GetUrl.as_view(), name="get_url"),

    # To delete the existing content.
    path("p/delete/", deleteUrl.as_view(), name="get_url"),

    # To get the token mapped with the given username , email nd password.
    path("p/getToken/", GetToken.as_view(), name="get_user"),

    # To get the user . input is token value
    path("p/getUser/", GetUser.as_view(), name="get_user"),

    # same as shortenurl but it gives new slug value everytime.
    path("p/create/", CreateNewPaste.as_view(), name="get_url"),

    # To get content mapped with the given slug value.
    path("p/get_content/", GetRawPaste.as_view(), name="get_url")
]


