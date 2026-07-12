from rest_framework import serializers
from .models import Aluno, Secretaria, Coordenador, Empresa, Tce, Estagio, RelatorioSemestral

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = 'username', 'email', 'first_name', 'last_name', 'matricula', 'unidade', 'telefone', 'cpf', 'dt_nascimento', 'procurando_estagio', 'horas_estagio', 'periodo', 'curso'

class SecretariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secretaria
        fields = 'username', 'email', 'first_name', 'last_name', 'matricula', 'unidade', 'carteira_de_trabalho'

class CoordenadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordenador
        fields = 'username', 'email', 'first_name', 'last_name', 'matricula', 'unidade', 'area'

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = 'id', 'razao_social', 'telefone', 'cep'

class TceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tce
        fields = 'status', 'apoliceseguro', 'bolsa', 'secretaria.id', 'aluno.matricula'

class EstagioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estagio
        fields = 'id', 'dtinicio', 'dtfim', 'tce.apoliceseguro', 'empresa.id'

class RelatorioSemestralSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatorioSemestral
        fields = 'status', 'data_envio', 'semestre', 'horas_estagiadas', 'coordenador.id', 'estagio.id'
