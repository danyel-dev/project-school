from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from escola.views import AlunosViewset, CursosViewset, MatriculasViewset

router = routers.DefaultRouter()
router.register('alunos', AlunosViewset, basename='Alunos')
router.register('cursos', CursosViewset, basename='Cursos')
router.register('matriculas', MatriculasViewset, basename='Matriculas')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
