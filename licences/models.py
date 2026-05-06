from django.db import models

class Licencia(models.Model):
    id = models.UUIDField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Licencia {self.id} - {'Activa' if self.is_active else 'Inactiva'}"
