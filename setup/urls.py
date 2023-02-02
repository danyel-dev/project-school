from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from escola.views import AlunosViewset, CursosViewset, MatriculasViewset


router = routers.DefaultRouter()

router.register('alunos', AlunosViewset)
router.register('cursos', CursosViewset)
router.register('matriculas', MatriculasViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
