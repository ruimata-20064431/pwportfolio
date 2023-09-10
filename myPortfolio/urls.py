"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    # home page / Hero page views
    path('', views.hero_page_view),

    # redirections representing site structure
    path('home', views.hero_page_view),
    path('about', views.about_page_view),
    path('projects', views.projects_page_view),
    path('web', views.web_page_view),
    path('blog', views.blog_page_view),
    path('contacts', views.contacts_page_view),
    
]