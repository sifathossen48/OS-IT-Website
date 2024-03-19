from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404


"""home view"""

def home(request):
    return render(request, 'index.html')