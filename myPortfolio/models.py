from django.db import models
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator  # chatgpt
import datetime



# Create your models here.
class Instituicao(models.Model):
    instituicaoID = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    nome = models.CharField(max_length = 50)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    cursoID = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    curso = models.CharField(max_length = 50)
    inicio = models.IntegerField (
        validators = [
            MinValueValidator(1980, message="Value must be 1980 or grater"),
            MaxValueValidator(datetime.datetime.now().year, message="Value cannot be greater than current year")
        ]
    )
    instituicao = models.ForeignKey(Instituicao, on_delete = models.CASCADE, related_name = 'cursos')

    def __str__(self):
        return self.curso #+ " | " #+ instituicao.nome[:25]


class Pessoa(models.Model):
    pessoaID = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    nome = models.CharField(max_length = 50)
    link = models.URLField(max_length = 200)

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    disciplinaID = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    nome = models.CharField(max_length = 50)
    ano = models.IntegerField(validators = [ MinValueValidator(0, message="deve introduzin um valor maior do que 0")])
    semestre = models.IntegerField(validators = [ MinValueValidator(0, message="deve introduzin um valor maior do que 0")])
    ects = models.IntegerField(validators = [ MinValueValidator(0, message="deve introduzin um valor maior do que 0")])
    topicos = models.CharField(max_length=50)
    professor = models.ManyToManyField(Pessoa, related_name='leciona')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='cadeiras')

    @property
    def periodo(self):
        return str(self.ano) + "/" + str(self.semestre)

    def __str__(self):
        return self.nome #+ ' | '  + curso.nome[:25]


class Imagem(models.Model):
    imagemID = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    nome = models.CharField(max_length = 50)
    imagem = models.ImageField(
        upload_to='myPortfolio/', 
        null=True, 
        blank=True
        )

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    projectID = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    nome = models.CharField(max_length = 50)
    descricao = models.CharField(max_length = 500, default = "")
    ano = models.IntegerField(validators = [ MinValueValidator(0, message="deve introduzin um valor maior do que 0")])
    cadeira = models.ForeignKey(Disciplina, on_delete=models.CASCADE, null = False)
    imagem = models.ForeignKey(Imagem, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome #+ ' | ' + cadeira.nome


class Tecnologia(models.Model):
    tecnologiaID = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    nome = models.CharField(max_length = 50)
    descricao = models.CharField(max_length = 200)

    def __str__(self):
        return self.nome


class Interesse(models.Model):
    interesseID = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    nome = models.CharField(max_length = 50)

    def __str__(self):
        return self.nome


class Competencia(models.Model):
    TECNICA = 1
    ORGANIZATIVA = 2
    SOCIAL = 3
    LINGUISTICA = 4

    TIPO_COMPETENCIAS = [
        (TECNICA, 'Técnica'),
        (ORGANIZATIVA, 'Organizativa'),
        (SOCIAL, 'Social'),
        (LINGUISTICA, 'Linguística')
    ]

    competenciaID = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    nome = models.CharField(max_length = 50)
    descricao = models.CharField(max_length = 200)
    tipocompetencia = models.IntegerField(
        choices = TIPO_COMPETENCIAS,
        default = TECNICA
    )
    projectos = models.ManyToManyField(Projeto, related_name = 'competencias')

    def __str__(self):
        return self.nome #f"{self.nome} - {str(tipocompetencia)}"
