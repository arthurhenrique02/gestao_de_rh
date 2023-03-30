from django.contrib import admin

from .models import ContabilizarHorasExtra


# criar model para HoraExtra em admin
class HoraExtraAdmin(admin.ModelAdmin):
    # mostra lista de elementos
    list_display = ["quantidade_horas", "motivo", "funcionario"]


# registrar model
admin.site.register(ContabilizarHorasExtra, HoraExtraAdmin)
