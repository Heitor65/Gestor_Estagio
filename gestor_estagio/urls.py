from rest_framework.routers import DefaultRouter
from .views import AlunoViewSet, SecretariaViewSet, CoordenadorViewSet, EmpresaViewSet, TceViewSet, EstagioViewSet, RelatorioSemestralViewSet

router = DefaultRouter()
router.register('alunos', AlunoViewSet)
router.register('secretarias', SecretariaViewSet)
router.register('coordenadores', CoordenadorViewSet)
router.register('empresas', EmpresaViewSet)
router.register('tces', TceViewSet)
router.register('estagios', EstagioViewSet)
router.register('relatorios', RelatorioSemestralViewSet)

urlpatterns = router.urls