from decouple import config
from django.contrib import admin
from django.urls import path

ADMIN_URL = config("ADMIN_URL")

urlpatterns = [
    path(ADMIN_URL, admin.site.urls),
]
