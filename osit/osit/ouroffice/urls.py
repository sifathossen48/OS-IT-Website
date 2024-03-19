from django.urls import path, re_path
from django.contrib import admin
from django.urls import path, re_path, include

from .views import ouroffice, new_office, particular_office, OfficeUpdateView

urlpatterns = [
    re_path(r'^ouroffice/new/$', new_office, name='new_office'),
    re_path(r'^ouroffice/(?P<pk>\d+)/$', particular_office, name='particular_office'),
    re_path(r'^ouroffice/(?P<pk>\d+)/edit/$', OfficeUpdateView.as_view(), name='edit_office'),
    re_path("ouroffice/", ouroffice, name="ouroffice"),
    re_path(r'^ouroffice/', ouroffice, name='ouroffice'),
    re_path("", include("tinymce.urls")),
    re_path('admin/', admin.site.urls)
]