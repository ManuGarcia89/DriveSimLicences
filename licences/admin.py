from django.contrib import admin
from .models import Licencia

@admin.register(Licencia)
class LicenciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha_vencimiento')
    search_fields = ('id',)
