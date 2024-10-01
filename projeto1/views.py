from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.contrib.auth import views as auth_views

class CustomLoginView(LoginView):
    template_name = 'home/login.html'  # Especifica o template para o login
    redirect_authenticated_user = True  # Redireciona usuários já autenticados
class CustomLogoutView(auth_views.LogoutView):
    template_name = 'home/logout.html'