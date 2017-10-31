from django.shortcuts import render
from django.utils import timezone
from .models import Exames, Paciente

# Create your views here.
def post_list(request):
	exames = Exames.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
	return render(request,'paginas/index.html', {'exames':exames})
def generic(request):
	if(request.method == 'POST'):
		paciente = Paciente.objects.all()
		cpf = request.POST.get('cpf')
		codigo   = request.POST.get('codigo')

		for paciente in paciente:
			if(paciente.getCodigo() == codigo and paciente.getCpf() == cpf):
				return render(request, paciente.getFile, {})
	return render(request,'paginas/generic.html',{})

def index(request):
	exames = Exames.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
	return render(request,'paginas/index.html', {'exames':exames})
def elements(request):
	return render(request,'paginas/elements.html', {})
def about(request):
	return render(request,'paginas/sobre.html', {})
