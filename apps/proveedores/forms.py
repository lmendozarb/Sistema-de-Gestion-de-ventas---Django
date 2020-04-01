from django import forms
from apps.proveedores.models import Proveedor
from apps.general.models import TipoDocumento

class ProveedorForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ProveedorForm, self).__init__(*args, **kwargs)
		self.fields['RazonSocial'].widget.attrs.update({'class': 'form-control'})
		self.fields['RUC'].widget.attrs.update({'class': 'form-control'})
		self.fields['DireccionLegal'].widget.attrs.update({'class': 'form-control'})
		self.fields['NombreContacto'].widget.attrs.update({'class': 'form-control'})
		self.fields['ApellidoContacto'].widget.attrs.update({'class': 'form-control'})
		self.fields['TipoDocumentoProveedor']=forms.ModelChoiceField(queryset=TipoDocumento.objects.filter(),initial=0)
		self.fields['TipoDocumentoProveedor'].widget.attrs.update({'class': 'custom-select'})
		self.fields['NroDocumentoProveeedor'].widget.attrs.update({'class': 'form-control'})
		self.fields['CorreoElectronico'].widget.attrs.update({'class': 'form-control'})
		self.fields['Movil'].widget.attrs.update({'class': 'form-control'})

	class Meta:
		model = Proveedor
		fields = [
		'RazonSocial',
		'RUC',
		'DireccionLegal',
		'NombreContacto',
		'ApellidoContacto',
		'TipoDocumentoProveedor',
		'NroDocumentoProveeedor',
		'CorreoElectronico',
		'Movil',
		]
		labels={
		'RazonSocial':"Razón Social",
		'RUC':"RUC",
		'DireccionLegal':"Dirección Fiscal",
		'NombreContacto':"Nombres del Contacto",
		'ApellidoContacto':"Apellidos del Contacto",
		'TipoDocumentoProveedor':"Tipo Documento",
		'NroDocumentoProveeedor':"Nro. Documento",
		'CorreoElectronico':"Correo Electrónico",
		'Movil':"Telefono Celular",
		}
