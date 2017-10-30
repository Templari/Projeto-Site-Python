from django.shortcuts import render
from django.utils import timezone
from .models import Exames

# Create your views here.
def post_list(request):
	exames = Exames.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
	return render(request,'paginas/index.html', {'exames':exames})
def generic(request):
	return render(request,'paginas/generic.html',{})
