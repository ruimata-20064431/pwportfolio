from .model import *


class deleteCurso(filterString):
    Curso.objects.filter(curso = filterString).delete()