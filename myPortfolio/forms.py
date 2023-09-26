from django.forms import ModelForm
from .models import *


class CompetenceForm(ModelForm):
    class Meta:
        model = Competencia
        fields = '__all__'

class CourseForm(ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'


class DisciplineForm(ModelForm):
    class Meta:
        model = Disciplina
        fields = '__all__'

class InstitutionForm(ModelForm):
    class Meta:
        model = Instituicao
        fields = '__all__'

class InterestForm(ModelForm):
    class Meta:
        model = Interesse
        fields = '__all__'

class PersonForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'

class ProjectForm(ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'

class TechnologyForm(ModelForm):
    class Meta:
        model = Tecnologia
        fields = '__all__'

