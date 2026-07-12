from django.shortcuts import render
from rest_framework import viewsets
from .models import Aluno, Secretaria, Coordenador, Empresa, Tce, Estagio, RelatorioSemestral
from .serializers import AlunoSerializer, SecretariaSerializer, CoordenadorSerializer, EmpresaSerializer, TceSerializer, EstagioSerializer, RelatorioSemestralSerializer


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

class EstagioViewSet(viewsets.ModelViewSet):
    queryset = Estagio.objects.all()
    serializer_class = EstagioSerializer

class RelatorioSemestralViewSet(viewsets.ModelViewSet):
    queryset = RelatorioSemestral.objects.all()
    serializer_class = RelatorioSemestralSerializer