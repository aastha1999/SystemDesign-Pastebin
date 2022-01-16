from datetime import datetime, timedelta
import uuid

import socket
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.timezone import now


class PasteFile(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    slug = models.SlugField(unique=True)
    date_time = models.DateTimeField(auto_now_add=True, blank=True)
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


