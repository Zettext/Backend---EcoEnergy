from django.db import models

class BaseModel(models.Model):
    ESTADOS = [
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo'),
    ]

    estado = models.CharField(max_length=10, choices=ESTADOS, default='ACTIVO')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


# =============================
# Modelos principales
# =============================
class Categoria(BaseModel):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Zona(BaseModel):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Dispositivo(BaseModel):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE)
    consumo_maximo = models.IntegerField()

    def __str__(self):
        return self.nombre

