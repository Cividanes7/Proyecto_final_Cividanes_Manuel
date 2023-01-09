"""project URL Configuration

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
from Cotizador.views import NeumaticoList, NeumaticoCrear, NeumaticoBorrar, NeumaticoActualizar, NeumaticoDetalle


urlpatterns = [
    path('admin/', admin.site.urls),
    path('panel-neumatico/<int:pk>/detalle', NeumaticoDetalle.as_view(), name='neumatico_detalle'),
    path('panel-neumatico/', NeumaticoList.as_view(), name='neumatico_list'),
    path('panel-neumatico/crear', NeumaticoCrear.as_view()),
    path('panel-neumatico/<int:pk>/borrar', NeumaticoBorrar.as_view()),
    path('panel-neumatico/<int:pk>/actualizar', NeumaticoActualizar.as_view()),
]
