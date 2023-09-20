from django.contrib import admin

from .models import Curso
from .models import Instituicao
from .models import Pessoa
from .models import Disciplina
from .models import Imagem
from .models import Projeto
from .models import Tecnologia
from .models import Interesse
from .models import Competencia


# Register your models here.
admin.site.register (Curso)
admin.site.register (Instituicao)
admin.site.register (Pessoa)
admin.site.register (Disciplina)
admin.site.register (Imagem)
admin.site.register (Projeto)
admin.site.register (Tecnologia)
admin.site.register (Interesse)
admin.site.register (Competencia) 