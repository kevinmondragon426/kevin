"""
URL configuration for casaberrio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    path('admin/', admin.site.urls, name='admin:home2'),
    path('', views.index, name='home'),
    path('home.html', views.index),
    path('login/', views.login_view, name='login'),
    path('login/register.html', views.register, name='register2'),
    path('login/login.html', views.login_view, name='register2'),
    path('nosotros.html', views.nosotros, name='nosotros'),
    path('pqrs.html', views.fidelizacion_view, name='pqrs'),
    path('home2.htmls', views.index),
    path('register/', views.register, name='register'),
    path('login.html', views.login_view, name='home_login'),
    path('register.html', views.register, name='register_login'),
    path('home/', views.home_two, name='home2'),
    path('home/reservas.html', views.reservas_view, name='reservas'),
    path('home/productos.html', views.productos),
    path('home/PSE.html', views.pse_view, name='tarjeta'),
    path('home/tarjetacd.html', views.tajetacd_view),
    path('home/alquiler.html', views.alquiler_view),
    path('home/pqrs.html', views.fidelizacion_view),
    path('home/nosotros.html', views.nosotros),
    path('home/home2.html', views.home_two),
    path('home/home2.htmls', views.home_two),
    path('home/home.html', LogoutView.as_view(), name='logout'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
