from django.shortcuts import render
from rest_framework import viewsets
from .models import Aluno, Secretaria, Coordenador, Empresa, Tce, Estagio, RelatorioSemestral
from .serializers import AlunoSerializer, SecretariaSerializer, CoordenadorSerializer, EmpresaSerializer, TceSerializer, EstagioSerializer, RelatorioSemestralSerializer
from .permissions import IsAluno, IsSecretaria, IsCoordenador
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

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

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsSecretaria]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsSecretaria]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [p() for p in permission_classes]

class RelatorioSemestralViewSet(viewsets.ModelViewSet):
    queryset = RelatorioSemestral.objects.all()
    serializer_class = RelatorioSemestralSerializer

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