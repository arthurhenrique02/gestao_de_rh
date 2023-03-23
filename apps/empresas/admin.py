from django.contrib import admin

from .models import Empresa

# adcionar model ao admin site
admin.site.register(Empresa)
