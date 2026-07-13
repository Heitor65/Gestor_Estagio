from django.core.exceptions import ValidationError
from brutils import is_valid_cep, is_valid_cpf, is_valid_cnpj
import re

def validar_semestre(semestre):

    if not re.fullmatch(r'\d{2}\.[12]', semestre):
        raise ValidationError(
            'O semestre deve estar no formato AA.1 ou AA.2. Exemplo: 26.1'
        )


def validar_cpf(cpf):

    cpf = cpf.replace('.', '').replace('-', '')

    if not is_valid_cpf(cpf):
        raise ValidationError('O CPF deve estar em um formato válido. Exemplo: 123.456.789-09')

def validar_cnpj(cnpj):

    cnpj = cnpj.replace('.', '').replace('/', '').replace('-', '')
    
    if not is_valid_cnpj(cnpj):
        raise ValidationError('O CNPJ deve estar em um formato válido. Exemplo: 12.345.678/0001-99')



def validar_matricula(matricula):

    if len(matricula) != 12:
        raise ValidationError('A matrícula deve conter exatamente 12 números')

    if not matricula.isdigit():
        raise ValidationError('A matrícula deve conter apenas números.')

    if not matricula.startswith('20'):
        raise ValidationError('A matrícula deve começar com 20.')



def validar_cep(cep):

    cep = cep.replace('-', '')

    if not cep.isdigit() or len(cep) != 8:
        raise ValidationError('O CEP deve conter 8 números. Exemplo: 22775033')

    if not is_valid_cep(cep):
        raise ValidationError('CEP inválido.')


def validar_periodo(periodo):


    if periodo < 1 or periodo > 10:
        raise ValidationError(
            'O período deve estar entre 1 e 10.'
        )


def validar_positivo(x):

    if x < 0:
        raise ValidationError(
            'O valor deve ser maior ou igual a zero.'
        )