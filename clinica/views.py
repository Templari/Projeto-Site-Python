from django.shortcuts import render
from django.utils import timezone
from .models import Exames, Paciente, ColetaAgendada

# Create your views here.
def post_list(request):
	exames = Exames.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
	return render(request,'paginas/index.html', {'exames':exames})
def generic(request):
	paciente = Paciente.objects.filter().values()
	cpf = request.POST.get('cpf')
	codigo   = request.POST.get('codigo')
	if(request.method == 'POST'):
		paciente = Paciente.objects.all()
		cpf = request.POST.get('cpf')
		codigo   = request.POST.get('codigo')
		return render(request,'paginas/generic.html', {'paciente':paciente,'codigo':codigo,'cpf':cpf})
	return render(request,'paginas/generic.html', {})
def index(request):
	exames = Exames.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
	return render(request,'paginas/index.html', {'exames':exames})
def elements(request):
	return render(request,'paginas/elements.html', {})
def about(request):
	return render(request,'paginas/sobre.html', {})
def consulta(request):
	consulta = ColetaAgendada()
	codigo = 0
	if(request.method == 'POST'):
		codigo = 1
		consulta.setNome(request.POST.get('nomecompleto'))
		consulta.setRua(request.POST.get('rua'))
		consulta.setBairro(request.POST.get('bairro'))
		consulta.setNumero(request.POST.get('numero'))
		consulta.setTelefone(request.POST.get('telefone'))
		consulta.setEmail(request.POST.get('email'))
		consulta.setComplemento(request.POST.get('complemento'))
		consulta.save()
		return render(request,'paginas/consulta.html',{'codigo':codigo})
	return render(request,'paginas/consulta.html',{'codigo':codigo})
