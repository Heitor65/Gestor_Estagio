from django.shortcuts import render
from rest_framework import viewsets
from .models import Aluno, Secretaria, Coordenador, Empresa, Tce, Estagio, RelatorioSemestral
from .serializers import AlunoSerializer, SecretariaSerializer, CoordenadorSerializer, EmpresaSerializer, TceSerializer, EstagioSerializer, RelatorioSemestralSerializer
from .permissions import IsAluno, IsSecretaria, IsCoordenador
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

    def get_permissions(self):
        if self.action == "list":
            return [IsSecretaria | IsCoordenador]

        if self.action == "create":
            return [IsSecretaria]

        if self.action == "retrieve":
            return [IsSecretaria | IsCoordenador]

        if self.action == "me":
            return [IsAluno]

        return [IsAuthenticated]

    @action(detail=False, methods=["get"])
    def me(self, request):
        serializer = self.get_serializer(request.user.aluno)
        return Response(serializer.data)

class SecretariaViewSet(viewsets.ModelViewSet):
    queryset = Secretaria.objects.all()
    serializer_class = SecretariaSerializer

class CoordenadorViewSet(viewsets.ModelViewSet):
    queryset = Coordenador.objects.all()
    serializer_class = CoordenadorSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class TceViewSet(viewsets.ModelViewSet):
    queryset = Tce.objects.all()
    serializer_class = TceSerializer

    def get_queryset(self):
        user = self.request.user

        if hasattr(user, 'aluno'):
            return Tce.objects.filter(aluno=user.aluno)

        if hasattr(user, 'secretaria'):
            return Tce.objects.all()

        return Tce.objects.none()    
    
    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAluno]
        elif self.action in ['partial_update', 'update']:
            permission_classes = [IsSecretaria]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [p() for p in permission_classes]
    
    @action(detail=True, methods=['post'], permission_classes=[IsSecretaria])
    def aprovar(self, request, pk=None):
        tce = self.get_object()
        tce.se_aprovar()
        return Response({'status': 'TCE aprovado'})

    @action(detail=True, methods=['post'], permission_classes=[IsSecretaria])
    def reprovar(self, request, pk=None):
        tce = self.get_object()
        tce.se_reprovar()
        return Response({'status': 'TCE reprovado'})

class EstagioViewSet(viewsets.ModelViewSet):
    queryset = Estagio.objects.all()
    serializer_class = EstagioSerializer

    def get_queryset(self):
        user = self.request.user

        if hasattr(user, 'aluno'):
            return Estagio.objects.filter(tce__aluno=user.aluno)
        
        if hasattr(user, 'secretaria'):
            return Estagio.objects.all()
        
        return Estagio.objects.none()

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsSecretaria]
        elif self.action in ['adicionar_relatorio']:
            permission_classes = [IsAluno]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsSecretaria]
        else:
            permission_classes = [IsAuthenticated]
        return permission_classes

    @action(detail=True, methods=['post'], permission_classes=[IsAluno], url_path='adicionar_relatorio')
    def adicionar_relatorio(self, request, pk=None):
        estagio = self.get_object()

        area = request.data.get('coordenador.area')

        if not area:
            return Response({'coordenador_area': 'Este campo é obrigatório.'}, status=400)

        try:
            coordenador = Coordenador.objects.get(area=area)
        except Coordenador.DoesNotExist:
            return Response({'coordenador': 'Coordenador não encontrado.'}, status=400)

        serializer = RelatorioSemestralSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(estagio=estagio, coordenador=coordenador)
    
        novo_relatorio = serializer.instance
        return Response(RelatorioSemestralSerializer(novo_relatorio).data,status=201)

class RelatorioSemestralViewSet(viewsets.ModelViewSet):
    queryset = RelatorioSemestral.objects.all()
    serializer_class = RelatorioSemestralSerializer

    def get_queryset(self):
        user = self.request.user

        if hasattr(user, 'aluno'):
            return RelatorioSemestral.objects.filter(estagio__tce__aluno=user.aluno)
        
        if hasattr(user, 'coordenador'):
            return RelatorioSemestral.objects.filter(coordenador=user.coordenador)
        
        if hasattr(user, 'secretaria'):
            return RelatorioSemestral.objects.all()

        return RelatorioSemestral.objects.none()

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAluno]
        elif self.action in ['partial_update', 'update']:
            permission_classes = [IsCoordenador]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [p() for p in permission_classes]
    
    @action(detail=True, methods=['post'], permission_classes=[IsCoordenador])
    def aprovar(self, request, pk=None):
        relatorio = self.get_object()
        relatorio.se_aprovar()
        return Response({'status': 'Relatório aprovado'})

    @action(detail=True, methods=['post'], permission_classes=[IsCoordenador])
    def reprovar(self, request, pk=None):
        relatorio = self.get_object()
        relatorio.se_reprovar()
        return Response({'status': 'Relatório reprovado'})