from django.urls import path, re_path
from django.contrib import admin

from .views import clients, new_client, delete_client

urlpatterns = [
    re_path(r'^clients/new/$', new_client, name='new_client'),
    re_path(r'^clients/delete/$', delete_client, name='delete_client'),
    re_path("clients/", clients, name="clients"),
    re_path('admin/', admin.site.urls)
]