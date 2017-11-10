from django.contrib import admin
from .models import Post, Paciente, ListaExames,ColetaAgendada
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('nome','idade', 'email') 
    search_fields = ('nome',)

#admin.site.register(Post)
admin.site.register(Paciente, ContactAdmin)
admin.site.register(ListaExames)
admin.site.register(ColetaAgendada)