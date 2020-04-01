from apps.perfil.models import Perfil
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group

def ProfileData(request):
	try:
		return {'ProfileData': get_object_or_404(Perfil, User=request.user.id),'Grupo':Group.objects.filter(user = request.user)} # of course some filter here
	except Exception as e:
		return {'ProfileData': ""} # of course some filter here



def needchangepass(request):
	try:
		perfil = get_object_or_404(Perfil, User=request.user.id)
		if not perfil.ChangePass:
			return {'needchangepass':1}
		else:
			return {'needchangepass':0}
	except Exception as e:
		return {'needchangepass':0}
