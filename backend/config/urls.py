from decouple import config
from django.conf import settings
from django.contrib import admin
from django.urls import path

if settings.DEBUG:
    ADMIN_URL = config("ADMIN_URL", default="admin/")
else:
    ADMIN_URL = config("ADMIN_URL")

urlpatterns = [
    path(ADMIN_URL, admin.site.urls),
]
