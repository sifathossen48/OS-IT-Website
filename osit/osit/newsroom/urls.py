from django.urls import path, re_path
from django.contrib import admin

from .views import newsroom, new_news, particular_news, NewsUpdateView, delete_news

urlpatterns = [
    re_path(r'^newsroom/new/$', new_news, name='new_news'),
    re_path(r'^newsroom/(?P<pk>\d+)/$', particular_news, name='particular_news'),
    re_path(r'^newsroom/(?P<pk>\d+)/edit/$', NewsUpdateView.as_view(), name='edit_news'),
    re_path(r'^newsroom/(?P<pk>\d+)/delete/$', delete_news, name='delete_news'),
    re_path("newsroom/", newsroom, name="newsroom"),
    re_path('admin/', admin.site.urls)
]

