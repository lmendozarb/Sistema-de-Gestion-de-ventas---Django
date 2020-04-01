from django.contrib import admin
from apps.clientes.models import Contacto
from apps.clientes.models import Clientes
# Register your models here.
admin.site.register(Contacto)
admin.site.register(Clientes)
