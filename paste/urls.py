from django.urls import path
from django.conf.urls import include

from .views import  CreateNewPaste, Detail, Index,  RawContent, GetUrl, find_url, GetRawPaste, deleteUrl
from paste.api.views import api_detail_paste_view

from accounts.api_account.views import registration_view

from rest_framework.authtoken.views import obtain_auth_token
# from .views import  Detail, Index,  RawContent, GetUrl, find_url, GetRawPaste

app_name = "paste"

urlpatterns = [
    path("api/get_content/", api_detail_paste_view, name="get_content"),

    path('api/account/register/', registration_view, name="register"),

    path('api/account/login/', registration_view, name="login"),

    path("", Index.as_view(), name="index"),
    path("<str:slug>/", Detail.as_view(), name="detail"),
    path('api/get_content/',include('paste.api.urls','paste_api')),
    # path("get_url/<str:content>/<str:title>/",Detail.as_view(),name="Post"),
    # path("p/<str:title>/", get_url.as_view(), name="thread"),
    path("raw/<str:slug>/", RawContent.as_view(), name="raw_content"),
    # path("find_url/<str:title>/<str:content>/", find_url.as_view(), name="url_link"),

    # path("shortenUrl", get_url.as_view(), name="get_url"),
    path("p/shortenUrl/", GetUrl.as_view(), name="get_url"),
    path("p/delete/", deleteUrl.as_view(), name="get_url"),
    
    path("p/create/", CreateNewPaste.as_view(), name="get_url"),
    path("p/get_content/", GetRawPaste.as_view(), name="get_url")
]


