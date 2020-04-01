from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.conf import settings
from apps.general.views import dashboard
from apps.general.views import changeforcepassword
from apps.cotizaciones.views import ProcessPayment

urlpatterns = [
	path("", login_required(dashboard), name="dashboard"),
	path('admin/', admin.site.urls),
	path("accounts/", include("django.contrib.auth.urls")),
	path("dashboard/", login_required(dashboard), name="dashboard"),
	path("clientes/", include(("apps.clientes.urls","clientes"), namespace="clientes")),
	path("cotizaciones/", include(("apps.cotizaciones.urls","cotizaciones"), namespace="cotizaciones")),
	path("items/", include(("apps.items.urls","items"), namespace="items")),
	path("proveedores/", include(("apps.proveedores.urls","proveedores"), namespace="proveedores")),
	path("generales/", include(("apps.general.urls","generales"), namespace="generales")),
	path("vilsoft/", include(("apps.vilsoft.urls","vilsoft"), namespace="vilsoft")),
	path("ordendecompra/", include(("apps.ordencompra.urls","ordencompra"), namespace="ordencompra")),
	path('changeforcepassword/',login_required(changeforcepassword), name="changeforcepassword"),
	path('processpayment/',ProcessPayment, name='processpayment'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
