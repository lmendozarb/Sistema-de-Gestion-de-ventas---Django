from django import forms

from apps.perfil.models import Perfil


class PerfilUsuarioForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(PerfilUsuarioForm, self).__init__(*args, **kwargs)
		self.fields['Foto'].widget.attrs.update({'class': 'form-control'})
		self.fields['movil'].widget.attrs.update({'class': 'form-control'})

	class Meta:
		model = Perfil
		fields = [
		'User',
		'Foto',
		'movil',
		]
		labels={
		'User':"Usuario",
		'Foto':"Foto",
		'movil':"Telefono Movil",
		}
