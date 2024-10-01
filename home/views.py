from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

