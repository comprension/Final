from django.urls import path
from .views import (
    HomeView,
    CreditosView,
    lista_categorias,
    crear_categoria,
    editar_categoria,
    lista_productos,
    crear_producto,
    editar_producto,
)

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='homeapp'),

    # Categorías
    path('categorias/', lista_categorias, name='categorias_listar'),
    path('categorias/nueva/', crear_categoria, name='categorias_crear'),
    path('categorias/<int:categoria_id>/editar/', editar_categoria, name='categorias_editar'),

    # Productos
    path('productos/', lista_productos, name='productos_listar'),
    path('productos/nuevo/', crear_producto, name='productos_crear'),
    path('productos/<int:producto_id>/editar/', editar_producto, name='productos_editar'),

    # Créditos
    path('creditos/', CreditosView.as_view(), name='creditos'),
]
