from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . import views

app_name = "home"

urlpatterns = [
    path("", views.index, name="index"),
    path("base/", views.base, name="base"),
    path("contactanos/", views.contactanos, name="contactanos"),
    
    # Autenticación y registro
    path("login/", auth_views.LoginView.as_view(template_name='home/login.html'), name="login"),
    path("logout/", LogoutView.as_view(next_page='home:login'), name="logout"),
    path("sign_up/", views.sign_up, name="sign_up"),
    
# Publicaciones y vistas generales
    path("noticia/", views.noticia, name="noticia"),
    path("perfil/", views.perfil, name="perfil"),
    path("crud_perfil/", views.crud_perfil, name="crud_perfil"),
    path("publicacion/", views.crear_publicacion, name="crear_publicacion"),
    path("categoria/", views.categoria, name="categoria"),
    
    # Módulo de usuarios (CRUD)
    path("crud_usuarios/", views.crud_usuarios, name="crud_usuarios"),
    path("crud_usuarios/crear/", views.crear_usuario, name="crear_usuario"),  # <--- Único con este nombre
    path("crud_usuarios/<int:pk>/editar/", views.editar_usuario, name="editar_usuario"),
    path("crud_usuarios/<int:pk>/bloquear/", views.bloquear_usuario, name="bloquear_usuario"),
    path("crud_usuarios/<int:pk>/eliminar/", views.eliminar_usuario, name="eliminar_usuario"),
    
    # Gestión de contenidos y contraseñas
    path("contraseña/", views.crud_cambiar_contrasena, name="crud_cambiar_contrasena"),
    
    path("comentario/", views.crud_comentarios, name="crud_comentarios"),
    path("crud_comentarios/<int:pk>/aprobar", views.aprobar_comentario, name="aprobar_comentario"),
    path("crud_comentarios/<int:pk>/bloquear", views.bloquear_comentario, name="bloquear_comentario"),
    path("crud_comentarios/<int:pk>/eliminar", views.eliminar_comentario, name="eliminar_comentario"),

    path("noticias/", views.crud_noticias, name="crud_noticias"),
    path("noticia/<int:pk>", views.noticia, name="noticia_detalle"),
    path("crud_noticias/<int:pk>/editar", views.editar_publicacion, name="editar_publicacion"),
    path("crud_noticias/<int:pk>/publicar", views.publicar_publicacion, name="publicar_publicacion"),
    path("crud_noticias/<int:pk>/eliminar", views.eliminar_publicacion, name="eliminar_publicacion"),

    path("categoria/<int:pk>", views.categoria, name="categoria_detalle"),
    path("categorias/", views.crud_categorias, name="crud_categorias"),
    path("crud_categorias/<int:pk>/editar/", views.editar_categoria, name="editar_categoria"),
    path("crud_categorias/<int:pk>/eliminar/", views.eliminar_categoria, name="eliminar_categoria"),
    path("editar_categoria/", views.editar_categoria, name="editar_categoria"),
]