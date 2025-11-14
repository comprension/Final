from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from .models import Categoria, Producto


# ---------- PÁGINAS ESTÁTICAS ----------

class HomeView(TemplateView):
    template_name = 'home.html'


class CreditosView(TemplateView):
    template_name = 'creditos.html'


# ---------- CATEGORÍAS ----------

def lista_categorias(request):
    categorias = Categoria.objects.all().order_by('id')
    return render(request, 'categorias_listar.html', {'categorias': categorias})


def crear_categoria(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion', '')

        if nombre:
            Categoria.objects.create(nombre=nombre, descripcion=descripcion)
            return redirect('home:categorias_listar')

    return render(request, 'categorias_form.html')


def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion', '')

        if nombre:
            categoria.nombre = nombre
            categoria.descripcion = descripcion
            categoria.save()
            return redirect('home:categorias_listar')

    return render(request, 'categorias_form.html', {'categoria': categoria})


# ---------- PRODUCTOS ----------

def lista_productos(request):
    productos = Producto.objects.select_related('categoria').all().order_by('id')
    return render(request, 'productos_listar.html', {'productos': productos})


def crear_producto(request):
    categorias = Categoria.objects.all().order_by('nombre')

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion', '')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock') or '0'
        categoria_id = request.POST.get('categoria')

        if nombre and precio and categoria_id:
            categoria = get_object_or_404(Categoria, id=categoria_id)
            try:
                stock_int = int(stock)
            except ValueError:
                stock_int = 0

            Producto.objects.create(
                nombre=nombre,
                descripcion=descripcion,
                precio=precio,
                stock=stock_int,
                categoria=categoria,
            )
            return redirect('home:productos_listar')

    return render(request, 'productos_form.html', {'categorias': categorias})


def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    categorias = Categoria.objects.all().order_by('nombre')

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion', '')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock') or '0'
        categoria_id = request.POST.get('categoria')

        if nombre and precio and categoria_id:
            categoria = get_object_or_404(Categoria, id=categoria_id)
            try:
                stock_int = int(stock)
            except ValueError:
                stock_int = 0

            producto.nombre = nombre
            producto.descripcion = descripcion
            producto.precio = precio
            producto.stock = stock_int
            producto.categoria = categoria
            producto.save()
            return redirect('home:productos_listar')

    contexto = {
        'producto': producto,
        'categorias': categorias,
    }
    return render(request, 'productos_form.html', contexto)
