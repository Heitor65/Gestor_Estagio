from django.contrib import admin
from .models import Usuario, Aluno, Secretaria, Coordenador, Empresa, Tce, RelatorioSemestral, Estagio

admin.site.register(Usuario)
admin.site.register(Aluno)
admin.site.register(Secretaria)
admin.site.register(Coordenador)
admin.site.register(Empresa)
admin.site.register(Tce)
admin.site.register(RelatorioSemestral)
admin.site.register(Estagio)