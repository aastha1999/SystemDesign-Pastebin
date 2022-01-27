from django.urls import path

from paste.api.views import api_detail_paste_view


app_name = "paste"

urlpatterns = [
    
    path("api/get_content/", api_detail_paste_view, name="get_content")
]