from django.conf import settings as conf_settings
from django.http import HttpResponse
from django.shortcuts import render
from django import template
from .dataforms import *
from .models import *
from .tables import *

#from .models import Instituicao

register = template.Library() # https://stackoverflow.com/questions/56725158/display-a-fixed-length-subset-of-a-list-in-a-django-template


#def index_view(request):
#    return HttpResponse('welcome to my portfolio')

def struct_page_view(request):
    return render(request, 'myPortfolio\struct.html')


# --- project views

def hero_page_view(request):
    return render(request, 'myPortfolio\home.html')

def about_page_view(request):  # TODO - new template to invoke
    return render(request, 'myPortfolio\\about.html')

def projects_page_view(request):
    return render(request, 'myPortfolio\projects.html')

def web_page_view(request):
    return render(request, 'myPortfolio\web.html')

def blog_page_view(request):
    return render(request, 'myPortfolio\\blog.html')

def contacts_page_view(request):
    return render(request, 'myPortfolio\contacts.html')



# ----- consolidates education view ----- 

## TODO
def consolidated_education_page_view(request):

    cursos = Curso.objects.all()
    cursos_table = CursoTable(cursos)
    cursos_title = 'My Courses'

    cadeiras = Disciplina.objects.all()
    cadeiras_table = DisciplinasTable(cadeiras)
    cadeiras_title = 'My Course Disciplines'
    
    projetos = Projeto.objects.all()
    projetos_table = ProjetoTable(projetos)
    projetos_title = 'My Discipline projects'

    pessoas = Pessoa.objects.all()
    pessoas_table = PessoaTable(pessoas)
    pessoas_title = 'My Beloved Teachers'

    courseForm = CourseForm(request.POST or None)
    if courseForm.is_valid():
        courseForm.save()
        courseForm = CourseForm()
    
    disciplineForm = DisciplineForm(request.POST or None)
    if disciplineForm.is_valid():
        disciplineForm.save()
        disciplineForm = DisciplineForm()
    
    projectForm = ProjectForm(request.POST or None)
    if projectForm.is_valid():
        projectForm.save()
        projectForm = ProjectForm()
    
    personForm = PersonForm(request.POST or None)
    if personForm.is_valid():
        personForm.save()
        personForm = PersonForm()

    context = {
        'title': 'EDUCATION PAGE',
        'cursos_title': cursos_title,
        'cursos': cursos_table,
        'cadeiras_title': cadeiras_title,
        'cadeiras':cadeiras_table,
        'projetos_title': projetos_title,
        'projetos': projetos_table,
        'pessoas_title': pessoas_title,
        'pessoas': pessoas_table,
        'courseForm': courseForm,
        'courseFormTitle': 'COURSE',
        'disciplineForm': disciplineForm,
        'disciplineFormTitle': 'DISCIPLINE',
        'projectForm': projectForm,
        'projectFormTitle': 'PROJECT',
        'personForm': personForm,
        'personFormTitle': 'TEACHER',
    }

    return render(request, 'myPortfolio/education/education.html', context)




# --- utils --- 

