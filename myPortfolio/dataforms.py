from django.shortcuts import render
#from .forms import TechnologiesForm
#from .forms import InstitutionForm
from .forms import *

# ----- Data management forms ----- 
def competence_form_view(request):
    record = CompetenceForm(request.POST or None)
    if record.is_valid():
        record.save()
    context = { 'form' : record, 'title' : 'Competence'}
    return render(request, 'myPortfolio/education/recordentry.html', context)

def course_form_view(request):
    record = CourseForm(request.POST or None)
    if record.is_valid():
        record.save()
    context = { 'form' : record, 'title' : 'Course'}
    return render(request, 'myPortfolio/education/recordentry.html', context)

def discipline_form_view(request):
    record = DisciplineForm(request.POST or None)
    if record.is_valid():
        record.save()
    context = { 'form' : record, 'title' : 'Discipline'}
    return render(request, 'myPortfolio/education/recordentry.html', context)

def institution_form_view(request):
    record = InstitutionForm(request.POST or None)
    if record.is_valid():
        record.save()
    context = { 'form' : record, 'title' : 'Institution'}
    return render(request, 'myPortfolio/education/recordentry.html', context)

def interest_form_view(request):
    record = InterestForm(request.POST or None)
    if record.is_valid():
        record.save()
    context = { 'form' : record, 'title' : 'Interest'}
    return render(request, 'myPortfolio/education/recordentry.html', context)

def person_form_view(request):
    record = PersonForm(request.POST or None)
    if record.is_valid():
        record.save()
    context = { 'form' : record, 'title' : 'Person'}
    return render(request, 'myPortfolio/education/recordentry.html', context)

def project_form_view(request):
    record = ProjectForm(request.POST or None)
    if record.is_valid():
        record.save()
    context = { 'form' : record, 'title' : 'Project'}
    return render(request, 'myPortfolio/education/recordentry.html', context)

def technology_form_view(request):
    record = TechnologyForm(request.POST or None)
    if record.is_valid():
        record.save()
    context = { 'form' : record, 'title' : 'Technology'}
    return render(request, 'myPortfolio/education/recordentry.html', context)

"""







def technology_form_view(request):

    technology = TechnologiesForm(request.POST or None)

    if technology.is_valid() and (technology.cleaned_data['nome'] != ""):
        technology.save()

    context = { 
        'form' : technology,
        'title' : 'Technology'
    }
    return render(request, 'myPortfolio/education/technologies.html', context) 


def institution_form_view(request):
    institution = InstitutionForm(request.POST or None)

    if institution.is_valid():
        institution.save()

    context = { 
        'form' : institution,
        'title' : 'Institution'
    }

    return render(request, 'myPortfolio/education/technologies.html', context)


def cursos_form_view(request):
    curso = CursoForm(request.POST or None)
    if curso.is_valid():
        curso.save()
    context = { 'form' : curso, 'title' : 'Curso'}
    return render(request, 'myPortfolio/education/technologies.html', context)



"""

# --- manage a simple form
"""
    intended to manage simple forms, in a standardized manner
    ->if a form require sepcific args, this must be reviewed (or a new general function must be created)
"""
"""


#--> no time to fix cleaned_data error (let's duplicate functions)
def create_form(request, target, TableForm, return_target):
    form  = TableForm(request.POST or None)
    if form.is_valid:
        form.save()
        form = TableForm()
        return HttpResponseRedirect(reverse(return_target))
    
    context = { 'form' : form }
    return render(request, target, context)
"""

"""
technology = TechnologiesForm(request.POST or None)

    if technology.is_valid():
        technology.save()

    context = { 'form' : technology}
    return render(request, 'myPortfolio/education/technologies.html', context) 
"""