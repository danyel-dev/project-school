from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = ['id', 'url', 'aluno', 'curso', 'periodo']


class AlunoSerializer(serializers.ModelSerializer):
    matricula_set = MatriculaSerializer(many = True)

    class Meta:
        model = Aluno
        fields = ['id', 'url', 'nome', 'rg', 'cpf', 'data_nascimento', 'matricula_set']


class CursoSerializer(serializers.ModelSerializer):
    matricula_set = MatriculaSerializer(many = True)

    class Meta:
        model = Curso
        fields = ['id', 'url', 'codigo_curso', 'descricao', 'nivel', 'matricula_set']
