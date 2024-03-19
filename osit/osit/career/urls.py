from django.urls import path, re_path

from .views import successView, careerView

urlpatterns = [
    re_path("career/", careerView, name="career"),
    re_path("success/", successView, name="success"),
]