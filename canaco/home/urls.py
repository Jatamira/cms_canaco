from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.index, name="index"),
    path("base/", views.base, name="base"),
    path("contactanos/", views.contactanos, name="contactanos"),
    path("categoria/", views.categoria, name="categoria"),
    path("login/", views.login, name="login"),
    path("noticia/", views.noticia, name="noticia"),
    path("perfil/", views.perfil, name="perfil"),
    path("sign_up/", views.sign_up, name="sign_up"),
    path("publicacion/", views.publicacion, name="publicacion"),
    path("usuario/", views.usuario, name="usuario"),
    path("contraseña/", views.contraseña, name="contraseña"),
    path("categorias/", views.categorias, name="categorias"),
    path("comentario/", views.comentario, name="comentario"),
    path("noticias/", views.noticias, name="noticias"),
    path("crud_perfil/", views.crud_perfil, name="crud_perfil"),
    path("usuarios/", views.usuarios, name="usuarios"),
    path("editar_categoria/", views.editar_categoria, name="editar_categoria"),
]