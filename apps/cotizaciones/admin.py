from django.contrib import admin
from apps.cotizaciones.models import CotizacionCabecera
from apps.cotizaciones.models import CuerpoCotizacion
from apps.cotizaciones.models import ItemPago
# Register your models here.
admin.site.register(CotizacionCabecera)
admin.site.register(CuerpoCotizacion)
admin.site.register(ItemPago)
