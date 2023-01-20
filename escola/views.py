from rest_framework import viewsets
from .models import Aluno, Curso
from serializer import AlunoSerializer, CursoSerializer


class AlunosSerializer(viewsets.ModelViewSet):
    """Exibindo todos os alunos"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursosSerializer(viewsets.ModelViewSet):
    """Exibindo todos os alunos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
