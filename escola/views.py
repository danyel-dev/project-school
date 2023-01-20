from rest_framework import viewsets
from .models import Aluno, Curso
from .serializer import AlunoSerializer, CursoSerializer


class AlunosViewset(viewsets.ModelViewSet):
    """Exibindo todos os alunos"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursosViewset(viewsets.ModelViewSet):
    """Exibindo todos os alunos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
