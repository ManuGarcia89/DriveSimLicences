from django.contrib import admin
from .models import Licencia

@admin.register(Licencia)
class LicenciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('id', 'descripcion')
