from django.db import models

# Modelos originales (se mantienen por compatibilidad)
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.nombre)


class Telefono(models.Model):
    tipo_telefono = (
        ('C', 'Casa'),
        ('M', 'Celular'),
        ('T', 'Trabajo'),
    )
    telefono = models.CharField(max_length=13)
    Estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=1, choices=tipo_telefono, default='C')
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.telefono)


# ---------- NUEVOS MODELOS PARA EL PROBLEMA ----------

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='productos')
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
