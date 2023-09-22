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


# --- utils ---
