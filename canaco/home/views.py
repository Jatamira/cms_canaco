from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def base(request):
    return render(request, 'home/base.html')

def contactanos(request):
    return render(request, 'home/contactanos.html')

def categoria(request):
    return render(request, 'home/categoria.html')

def login(request):
    return render(request, 'home/login.html')

def noticia(request):
    return render(request, 'home/noticia.html')

def perfil(request):
    return render(request, 'home/perfil.html')

def sign_up(request):
    return render(request, 'home/sign_up.html')

def publicacion(request):
    return render(request, 'home/crear_publicacion.html')

def usuario(request):
    return render(request, 'home/crear_usuario.html')

def contraseña(request):
    return render(request, 'home/crud_cambiar_contrasena.html')

def categorias(request):
    return render(request, 'home/crud_categorias.html')

def comentario(request):
    return render(request, 'home/crud_comentarios.html')

def noticias(request):
    return render(request, 'home/crud_noticias.html')

def crud_perfil(request):
    return render(request, 'home/crud_perfil.html')

def usuarios(request):
    return render(request, 'home/crud_usuarios.html')

def editar_categoria(request):
    return render(request, 'home/editar_categoria.html')