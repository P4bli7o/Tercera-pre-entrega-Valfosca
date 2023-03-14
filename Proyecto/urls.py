"""Proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from AppValfosca.views import index, venta_mayorista, registrar_mayoristas, venta_minorista, registrar_minorista, pedidos, registrar_pedidos, cancelacion_pedidos, registrar_cancelaciones, busqueda, buscar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = "index"),
    path('venta-mayorista/', venta_mayorista, name = "mayorista"),
    path('venta-mayorista/registrar', registrar_mayoristas, name = "registro_mayorista"),
    path('venta-minorista/', venta_minorista, name = "minorista"),
    path('venta-minorista/registrar', registrar_minorista, name = "registro_minorista"),
    path('pedidos/', pedidos, name = "pedidos"),
    path('pedidos/registrar', registrar_pedidos, name = "registro_pedidos"),
    path('cancelaciones/', cancelacion_pedidos, name = "cancelar"),
    path('cancelaciones/registrar', registrar_cancelaciones, name = "registro_cancelaciones"),
    path('busqueda/', busqueda, name = "buscar"),
    path('busqueda/buscar', buscar, name = "buscar-datos"),
    

]
