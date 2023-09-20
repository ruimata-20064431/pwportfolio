from django.conf import settings as conf_settings
from django.http import HttpResponse
from django.shortcuts import render
from .models import Tecnologia
from .models import Instituicao

# Create your views here.
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
    return render(request, 'myPortfolio/education.html')




# --- utils --- 


