from django.db import models

class StatusDocumento(models.TextChoices):
    PENDENTE = 'pendente', 'Pendente'
    APROVADO = 'aprovado', 'Aprovado'
    REPROVADO = 'reprovado', 'Reprovado'


class UNIDADE_CHOICES(models.TextChoices):
    BARRA = 'barra', 'Barra'
    BOTAFOGO = 'botafogo', 'Botafogo'

class AREA_CHOICES(models.TextChoices):
    NEGOCIOS = 'negocios', 'Negócios'
    TECNOLOGIA = 'tecnologia', 'Tecnologia'
    FINANCAS = 'financas', 'Finanças'
    DIREITO = 'direito', 'Direito'
    ENGENHARIA = 'engenharia', 'Engenharia'

class CURSOS_CHOICES(models.TextChoices):
    ADMINISTRACAO = 'administração', 'Administração'
    ANALISE_DESENVOLVIMENTO_SISTEMAS = 'analise e desenvolvimento de sistemas', 'Análise e Desenvolvimento de Sistemas'
    ARQUITETURA_URBANISMO = 'arquitetura e urbanismo', 'Arquitetura e Urbanismo'
    CIENCIA_DADOS_INTELIGENCIA_ARTIFICIAL = 'ciencia de dados e inteligencia artificial', 'Ciência de Dados e Inteligência Artificial'
    CIENCIAS_CONTABEIS = 'ciencias contabeis', 'Ciências Contábeis'
    DIREITO = 'direito', 'Direito'
    CIENCIAS_ECONOMICAS = 'ciencias economicas', 'Ciências Econômicas'
    COMUNICACAO_SOCIAL_PUBLICIDADE_PROPAGANDA = 'comunicacao social - publicidade e propaganda', 'Comunicação Social - Publicidade e Propaganda'
    ENGENHARIA_CIVIL = 'engenharia civil', 'Engenharia Civil'
    ENGENHARIA_PRODUCAO = 'engenharia de producao', 'Engenharia de Produção'
    ENGENHARIA_COMPUTACAO = 'engenharia da computacao', 'Engenharia da Computação'
    ENGENHARIA_SOFTWARE = 'engenharia de software', 'Engenharia de Software'
    RELACOES_INTERNACIONAIS = 'relacoes internacionais', 'Relações Internacionais'