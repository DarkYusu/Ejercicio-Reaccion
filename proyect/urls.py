"""proyect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tiemporespuesta.views import SignupView, dashboard, jugar, ver_ranking, mi_puntuacion, guardar_prueba

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', SignupView.as_view(), name='signup'),
    path('', dashboard, name='dashboard'),
    path('jugar/', jugar, name='jugar'),
    path('ver-ranking/', ver_ranking, name='ver_ranking'),
    path('mi-puntuacion/', mi_puntuacion, name='mi_puntuacion'),
    path('guardar-prueba/', guardar_prueba, name='guardar_prueba'),  # Agregado aquí
]