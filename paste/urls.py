from django.urls import path

from .views import  CreateNewPaste, Detail, Index,  RawContent, GetUrl, find_url, GetRawPaste, deleteUrl
# from .views import  Detail, Index,  RawContent, GetUrl, find_url, GetRawPaste

app_name = "paste"

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("<str:slug>/", Detail.as_view(), name="detail"),
    # path("get_url/<str:content>/<str:title>/",Detail.as_view(),name="Post"),
    # path("p/<str:title>/", get_url.as_view(), name="thread"),
    path("raw/<str:slug>/", RawContent.as_view(), name="raw_content"),
    path("find_url/<str:title>/<str:content>/", find_url.as_view(), name="url_link"),

    # path("shortenUrl", get_url.as_view(), name="get_url"),
    path("shortenUrl/", GetUrl.as_view(), name="get_url"),
    path("deleteUrl/", deleteUrl.as_view(), name="get_url"),
    
    path("p/create/", CreateNewPaste.as_view(), name="get_url"),
    path("p/<str:slug>", GetRawPaste.as_view(), name="get_url")
]


