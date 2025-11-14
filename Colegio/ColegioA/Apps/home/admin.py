from django.contrib import admin
from .models import Estudiante, Curso, Telefono, Categoria, Producto

admin.site.register(Estudiante)
admin.site.register(Curso)
admin.site.register(Telefono)
admin.site.register(Categoria)
admin.site.register(Producto)
