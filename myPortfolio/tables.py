from django_tables2 import tables
from .forms import *
from .models import *

import itertools


class CursoTable(tables.Table):
    class Meta:
        model = Curso
        fields = ['id', 'cursoID', 'curso', 'inicio', ] # 'instituicao',]
        exclude = ("id", "cursoID", )
        orderable = False



class DisciplinasTable(tables.Table):
    periodo = tables.columns.Column('Semestre', )
    class Meta:
        model = Disciplina
        attrs = {'class': 'table'}
        fields = ['id', 'disciplinaID', 'nome', 'ano', 'semestre', 'periodo', 'ects', 'topicos', 'professor', 'curso']
        exclude = ('id', 'disciplinaID', 'ano', 'semestre')
        orderable = False


class ProjetoTable(tables.Table):
    class Meta:
        model = Projeto
        fields = {'id', 'projectID', 'nome', 'descricao', 'ano', 'cadeira', 'imagem'}
        exclude = ('id', 'projectID', )
        sequence = ('nome', 'ano', 'cadeira', 'descricao')
        orderable = False
        

class PessoaTable(tables.Table):
    class Meta: 
        model = Pessoa
        fields = {'id', 'pessoaID', 'nome', 'link',}
        exclude = ('id', 'pessoaID',)
        sequence = ('nome', 'link',)
        orderable = False