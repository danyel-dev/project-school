from rest_framework import viewsets, generics
from .models import Aluno, Curso, Matricula
from .serializer import AlunoSerializer, AlunoSerializerV2, CursoSerializer, MatriculaSerializer, ListaMatriculasALunoSerializer, ListaMatriculasCursoSerializer


class AlunosViewset(viewsets.ModelViewSet):
    """Exibindo todos os alunos"""
    queryset = Aluno.objects.all()
    def get_serializer_class(self):
        if self.request.version == 'V2':
            return AlunoSerializerV2
        return AlunoSerializer
    

class CursosViewset(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class MatriculasViewset(viewsets.ModelViewSet):
    """Exibindo todas as matriculas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


class ListaMatriculasALuno(generics.ListAPIView):
    """Exibindo todas as matriculas de um aluno"""
    serializer_class = ListaMatriculasALunoSerializer

    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id = self.kwargs['pk'])
        return queryset


class ListaMatriculasCurso(generics.ListAPIView):
    """Exibindo todas as matriculas de um aluno"""
    serializer_class = ListaMatriculasCursoSerializer

    def get_queryset(self):
        return Matricula.objects.filter(curso_id = self.kwargs['pk'])
