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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from Cotizador.views import NeumaticoList, NeumaticoCrear, NeumaticoBorrar, NeumaticoActualizar, NeumaticoDetalle
from Functions.views import (index, PostDetalle, PostListar, 
                               PostCrear, PostBorrar, PostActualizar,
                               UserSignUp, UserLogin, UserLogout, 
                               AvatarActualizar, UserActualizar, MensajeCrear, MensajeListar, MensajeDetalle)
from django.contrib.admin.views.decorators import staff_member_required
from Functions.views import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('panel-neumatico/<int:pk>/detalle', NeumaticoDetalle.as_view()),
    path('panel-neumatico/', NeumaticoList.as_view()),
    path('panel-neumatico/crear', NeumaticoCrear.as_view()),
    path('panel-neumatico/<int:pk>/borrar', NeumaticoBorrar.as_view()),
    path('panel-neumatico/<int:pk>/actualizar', NeumaticoActualizar.as_view()),
    path('success_updated_message/',TemplateView.as_view(template_name="ejemplo/success_updated_message.html")),
    path('Functions/', index, name="Functions-index"),
    path('Functions/<int:pk>/detalle/', PostDetalle.as_view(), name="Functions-detalle"),
    path('Functions/listar/', PostListar.as_view(), name="Functions-listar"),
    path('Functions/crear/', staff_member_required(PostCrear.as_view()), name="Functions-crear"),
    path('Functions/<int:pk>/borrar/', staff_member_required(PostBorrar.as_view()), name="Functions-borrar"),
    path('Functions/<int:pk>/actualizar/', staff_member_required(PostActualizar.as_view()), name="Functions-actualizar"),
    path('Functions/signup/', UserSignUp.as_view(), name ="Functions-signup"),
    path('Functions/login/', UserLogin.as_view(), name= "Functions-login"),
    path('Functions/logout/', UserLogout.as_view(), name="Functions-logout"),
    path('Functions/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="Functions-avatars-actualizar"),
    path('Functions/users/<int:pk>/actualizar/', UserActualizar.as_view(), name="Functions-users-actualizar"),
    path('Functions/mensajes/crear/', MensajeCrear.as_view(), name="Functions-mensajes-crear"),
    path('Functions/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name="Functions-mensajes-detalle"),
    path('Functions/mensajes/listar/', MensajeListar.as_view(), name="Functions-mensajes-listar"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)