from django import forms
from apps.vilsoft.models import DatosEmpresa
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , UserChangeForm


class EnterpriseDataForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(EnterpriseDataForm, self).__init__(*args, **kwargs)
		self.fields['Nombre'].widget.attrs.update({'class': 'form-control'})
		self.fields['NickName'].widget.attrs.update({'class': 'form-control'})
		self.fields['Direccion'].widget.attrs.update({'class': 'form-control'})
		self.fields['Website'].widget.attrs.update({'class': 'form-control'})
		self.fields['Mail'].widget.attrs.update({'class': 'form-control'})
		self.fields['RUC'].widget.attrs.update({'class': 'form-control'})
		self.fields['Telefono'].widget.attrs.update({'class': 'form-control'})


	class Meta:
		model = DatosEmpresa
		fields = [
			'Nombre',
			'NickName',
			'Direccion',
			'Website',
			'Mail',
			'RUC',
			'Telefono',
		]
		labels = {
			'NOmbre':"Razón social",
			'NickName':"Nombre Comercial",
			'Direccion':"Dirección Fiscal",
			'Website':"Sitio Web",
			'Mail':"Correo Contacto",
			'RUC':"RUC",
			'Telefono':"Telefono",
		}


class UserForm(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({'class': 'form-control','required':'required'})
		self.fields['first_name'].widget.attrs.update({'class': 'form-control','required':'required'})
		self.fields['last_name'].widget.attrs.update({'class': 'form-control','required':'required'})
		self.fields['email'].widget.attrs.update({'class': 'form-control','required':'required'})
		self.fields['password1'].widget.attrs.update({'class': 'form-control','required':'required','type':'password'})
		self.fields['password2'].widget.attrs.update({'class': 'form-control','required':'required','type':'password'})


	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2',
		]

class UserEditForm(UserChangeForm):
	def __init__(self, *args, **kwargs):
		super(UserEditForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({'class': 'form-control','required':'required'})
		self.fields['first_name'].widget.attrs.update({'class': 'form-control','required':'required'})
		self.fields['last_name'].widget.attrs.update({'class': 'form-control','required':'required'})
		self.fields['email'].widget.attrs.update({'class': 'form-control','required':'required'})

	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
		]
