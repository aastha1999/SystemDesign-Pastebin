from django.contrib import admin

# from .models import Comment, PasteFile
from .models import PasteFile, Account

from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ['user']

admin.site.register(PasteFile)
admin.site.register(Account)
# admin.site.register(Comment)
