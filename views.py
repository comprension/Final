from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Video, UsuarioPublico
from .forms import VideoForm, UsuarioPublicoForm

def home(request):
    return render(request, 'home.html')

def videos_lista(request):
    data = Video.objects.order_by('-fecha_publicacion', 'titulo')
    return render(request, 'videos/lista.html', {'videos': data})

def video_crear(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('cursos:videos_lista'))
    else:
        form = VideoForm()
    return render(request, 'videos/form.html', {'form': form})

def usuarios_lista(request):
    data = UsuarioPublico.objects.order_by('-fecha_registro', 'apellido', 'nombre')
    return render(request, 'usuarios/lista.html', {'usuarios': data})

def usuario_crear(request):
    if request.method == 'POST':
        form = UsuarioPublicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('cursos:usuarios_lista'))
    else:
        form = UsuarioPublicoForm()
    return render(request, 'usuarios/form.html', {'form': form})

def creditos(request):
    return render(request, 'creditos.html')
