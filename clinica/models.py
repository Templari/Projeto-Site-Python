from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class ListaExames(models.Model):
    icon = models.FileField(upload_to='exames/icons', blank=True)
    title = models.CharField(max_length=40, null=True)
    descrip = models.TextField(max_length=150, null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def __str__(self):
        return self.title

class Paciente(models.Model):
    author = models.ForeignKey('auth.User')
    nome = models.CharField('Nome Completo',max_length=200)
    cpf = models.CharField('CPF', max_length=11,unique=True)
    codigo = models.CharField('Codigo',max_length=11,unique=True,null=True)
    idade = models.IntegerField()
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True)
    criado_em = models.DateTimeField('criado em', auto_now_add=True)
    file = models.FileField(upload_to='pacientes/exames',blank=True)


    def getCodigo(self):
        return self.codigo
    def setCodigo(self,codigo=''):
        self.codigo=codigo
    def getCpf(self):
        return self.cpf
    def setCpf(self,cpf=''):
        self.cpf=cpf
    def getFile(self):
        return self.file    
    class Meta:
        ordering = ['criado_em']
        verbose_name = (u'nome')
        verbose_name_plural = (u'Pacientes')
    
    def __str__(self):
        return self.nome

class ColetaAgendada(models.Model):
    rua = models.CharField("Rua", max_length=50,null=False)
    numero = models.CharField("Numero",max_length=20,null=False)
    bairro = models.CharField("Bairro",max_length=50, null=False)
    complemento = models.CharField("Complemento", max_length=100, null=False)
    telefone = models.IntegerField("Telefone",null=False)
    email = models.EmailField("Email",null=False)
    nome = models.CharField("Nome Completo",max_length=50,null=False)


    def setRua(self,rua=''):
        self.rua = rua
    def getRua(self):
        return self.rua
    def setBairro(self,bairro=''):
        self.bairro = bairro
    def getBairro(self):
        return self.bairro
    def setNumero(self,numero=''):
        self.numero = numero
    def getNumero(self):
        return self.numero
    def setComplemento(self,complemento=''):
        self.complemento = complemento
    def getComplemento(self):
        return self.complemento
    def setTelefone(self,telefone=''):
        self.telefone = telefone
    def getTelefone(self):
        return self.telefone
    def setEmail(self,email=''):
        self.email = email
    def getEmail(self):
        return self.email
    def setNome(self,nome=''):
        self.nome = nome
    def getNome(self):
        return self.nome


#class Postagem(models.Model):
#    titulo = models.CharField(max_length=100,blank=False)
#    imagem = models.ImageField(upload_to = "blog/uploads/postagem",blank=True)
#   conteudo = models.TextField()
#    data = models.DateField() 
#    status = models.CharField(
#        max_length=1,
#        default=artigos,
#        choices=menu,
#        blank=False,
#        null=True,
#    )

#    def __unicode__(self):
#        return "%s - %s - %s" % (self.data,self.titulo,self.conteudo)