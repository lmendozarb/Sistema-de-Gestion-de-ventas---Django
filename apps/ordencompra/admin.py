from django.contrib import admin
from apps.ordencompra.models import OrdenCabecera
from apps.ordencompra.models import OrdenCompraBody
from apps.ordencompra.models import OrdenCompraCierre
# Register your models here.
admin.site.register(OrdenCabecera)
admin.site.register(OrdenCompraBody)
admin.site.register(OrdenCompraCierre)
