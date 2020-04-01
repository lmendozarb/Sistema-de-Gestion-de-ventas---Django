from django.contrib import admin
from apps.general.models import TipoDocumento
from apps.general.models import Moneda
# Register your models here.
admin.site.register(TipoDocumento)
admin.site.register(Moneda)
