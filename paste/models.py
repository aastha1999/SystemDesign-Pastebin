from datetime import datetime, timedelta
import uuid

import socket
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.timezone import now

# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token



class PasteFile(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    slug = models.SlugField(unique=True)
    date_time = models.DateTimeField(auto_now_add=True, blank=True)
    # email = models.EmailField(unique=True)
    # username = models.TextField(unique=True)
    # password = models.TextField()
    # password2 = models.TextField()
    # host = socket.gethostname()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # host = socket.gethostname()
        # return reverse("paste:detail", kwargs={"host":self.host,"slug": self.slug})
        return reverse("paste:detail", kwargs={"slug": self.slug})

    def get_slug(self):
        uuid_value = str(uuid.uuid4())
        unique_slug = slugify(uuid_value[0:13])
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_slug()
        return super(PasteFile, self).save(*args, **kwargs)

# from django.contrib.auth.models import AbstractUser
class Account(models.Model):
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('email','username','password','password2')

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender,instance=None, created = False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
