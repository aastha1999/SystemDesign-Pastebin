from django.urls import path

from accounts.api_account.views import (registration_view,)


app_name = "accounts"

urlpatterns = [
    
    path('register', registration_view, name="register")
]