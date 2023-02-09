from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula


class MatriculaSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    aluno = serializers.ReadOnlyField(source='aluno.nome')
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ['id', 'url', 'aluno', 'curso', 'periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()


class AlunoSerializer(serializers.ModelSerializer):
    matricula_set = MatriculaSerializer(many = True)

    class Meta:
        model = Aluno
        fields = ['id', 'url', 'nome', 'rg', 'cpf', 'data_nascimento', 'matricula_set']


class AlunoSerializerV2(serializers.ModelSerializer):
    matricula_set = MatriculaSerializer(many = True)

    class Meta:
        model = Aluno
        fields = ['id', 'url', 'nome', 'rg', 'cpf', 'celular', 'data_nascimento', 'matricula_set']


class CursoSerializer(serializers.ModelSerializer):
    matricula_set = MatriculaSerializer(many = True)

    class Meta:
        model = Curso
        fields = ['id', 'url', 'codigo_curso', 'descricao', 'nivel', 'matricula_set']


class ListaMatriculasALunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()


class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    aluno = serializers.ReadOnlyField(source='aluno.nome')
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ['aluno', 'periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()