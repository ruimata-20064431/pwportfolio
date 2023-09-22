from django_tables2 import tables
from .forms import *
from .models import *

import itertools


class CursoTable(tables.Table):
    class Meta:
        model = Curso
        fields = ['id', 'cursoID', 'curso', 'inicio']
        exclude = ("id", "cursoID", )



class DisciplinasTable(tables.Table):
    periodo = tables.columns.Column('Semestre', )
    class Meta:
        model = Disciplina
        attrs = {'class': 'table'}
        fields = ['id', 'disciplinaID', 'nome', 'ano', 'semestre', 'periodo', 'ects', 'topicos', 'professor', 'curso']
        exclude = ('id', 'disciplinaID', 'ano', 'semestre')


