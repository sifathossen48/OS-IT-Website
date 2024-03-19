from django.urls import path, re_path
from django.contrib import admin

from .views import solution, solution_product, new_solution, new_product, specific_product, ProductUpdateView, delete_product

urlpatterns = [
    re_path(r'^solution/new/$', new_solution, name='new_solution'),
    re_path(r'^solution/(?P<pk>\d+)/product/(?P<product_pk>\d+)/$', solution_product, name='solution_product'),
    re_path(r'^solution/(?P<pk>\d+)/$', solution_product, name='solution_product'),
    re_path(r'^solution/(?P<pk>\d+)/new/$', new_product, name='new_product'),
    re_path(r'^solution/product/(?P<pk>\d+)/product/(?P<product_pk>\d+)/$', specific_product, name='specific_product'),
    re_path(r'^solution/product/(?P<pk>\d+)/product/(?P<product_pk>\d+)/edit/$', ProductUpdateView.as_view(), name='edit_product'),
    re_path(r'^solution/product/(?P<pk>\d+)/product/(?P<product_pk>\d+)/delete/$', delete_product, name='delete_product'),
    re_path("solution/", solution, name="solution"),
    re_path('admin/', admin.site.urls)
]