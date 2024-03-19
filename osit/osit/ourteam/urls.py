from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static


from .views import ourteam, new_team, ourteam_teammember, new_member, individual_member, MemberUpdateView, delete_member

urlpatterns = [
    re_path(r'^ourteam/new/$', new_team, name='new_team'),
    re_path(r'^ourteam/(?P<pk>\d+)/teammember/(?P<teammember_pk>\d+)/$', ourteam_teammember, name='ourteam_teammember'),
    re_path(r'^ourteam/(?P<pk>\d+)/$', ourteam_teammember, name='ourteam_teammember'),
    re_path(r'^ourteam/(?P<pk>\d+)/new/$', new_member, name='new_member'),
    re_path(r'^ourteam/teamember/(?P<pk>\d+)/teammember/(?P<teammember_pk>\d+)/$', individual_member, name='individual_member'),
    re_path(r'^ourteam/teammember/(?P<pk>\d+)/teammember/(?P<teammember_pk>\d+)/edit/$', MemberUpdateView.as_view(), name='edit_member'),
    re_path(r'^ourteam/teammember/(?P<pk>\d+)/teammember/(?P<teammember_pk>\d+)/delete/$', delete_member, name='delete_member'),
    # re_path("ourteam/", ourteam, name="ourteam"),
    re_path(r'^ourteam/', ourteam, name='ourteam'),
    re_path('admin/', admin.site.urls)
    
]

# Add the following line to serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

