from rest_framework import serializers
from .models import Usuario, Aluno, Secretaria, Coordenador, Empresa, Tce, Estagio, RelatorioSemestral

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = (
            "matricula",
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "unidade",
        )
        extra_kwargs = {
            "password": {"write_only": True}
        }

class AlunoSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model = Aluno
        fields = (
            "usuario",
            "telefone",
            "cpf",
            "dt_nascimento",
            "procurando_estagio",
            "horas_estagio",
            "periodo",
            "curso",
        )

    def create(self, validated_data):
        usuario_data = validated_data.pop("usuario")
        password = usuario_data.pop("password")

        usuario = Usuario.objects.create_user(
            password=password,
            **usuario_data
        )

        return Aluno.objects.create(
            usuario=usuario,
            **validated_data
        )

class SecretariaSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()
    
    class Meta:
        model = Secretaria
        fields = (
            "usuario",
            "carteira_de_trabalho",
            )
    
    def create(self, validated_data):
        usuario_data = validated_data.pop("usuario")
        password = usuario_data.pop("password")
    
        usuario = Usuario.objects.create_user(
            password=password,
            **usuario_data
            )
    
        return Secretaria.objects.create(
            usuario=usuario,
            **validated_data
            )

class CoordenadorSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model = Coordenador
        fields = ('usuario', 
                  'area', 
                  )

    def create(self, validated_data):
            usuario_data = validated_data.pop("usuario")
            password = usuario_data.pop("password")
        
            usuario = Usuario.objects.create_user(
                password=password,
                **usuario_data
                )
        
            return Coordenador.objects.create(
                usuario=usuario,
                **validated_data
                )

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ('id', 
                  'razao_social', 
                  'telefone', 
                  'cep',
                  'uf',
                  'cidade',
                  'log',
                  'comp',
                  'num',
                  'bairro',
                  'cnpj'
                  )
        read_only_fields = ['id']

class TceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tce
        fields = ('status', 
                  'apoliceseguro', 
                  'bolsa',
                  'secretaria',
                  'aluno',
                  )

class EstagioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estagio
        fields = ('id', 
                  'dtinicio', 
                  'dtfim', 
                  'tce',
                  'cargahorariasemanal',
                  'empresa'
                  )
        read_only_fields = ['id']

class RelatorioSemestralSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatorioSemestral
        fields = ('status', 
                  'data_envio', 
                  'semestre', 
                  'horas_estagiadas',
                  'estagio'
                  )
        read_only_fields = ['estagio']
