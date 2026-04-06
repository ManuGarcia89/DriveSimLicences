from django.db import models

class Licencia(models.Model):
    id = models.UUIDField(primary_key=True)
    fecha_vencimiento = models.DateField()

    def __str__(self):
        return f"Licencia {self.id} - Vence: {self.fecha_vencimiento}"
