from django.conf.urls import url
from .views import index
from .views import aluno
from .views import exercicio
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^aluno/adicionar$', aluno.adicionar, name='aluno_adicionar'),
    url(r'^aluno/editar/(?P<pk>\d+)$', aluno.editar, name='aluno_editar'),
    url(r'^aluno/apagar/(?P<pk>\d+)$', aluno.apagar, name='aluno_apagar'),
    url(r'^aluno/detalhar/(?P<pk>\d+)$', aluno.detalhar, name='aluno_detalhar'),
    url(r'^aluno$', aluno.listar, name='aluno_listar'),
    url(r'^exercicio/adicionar$', exercicio.adicionar, name='exercicio_adicionar'),
    url(r'^exercicio/editar/(?P<pk>\d+)$', exercicio.editar, name='exercicio_editar'),
    url(r'^exercicio/apagar/(?P<pk>\d+)$', exercicio.apagar, name='exercicio_apagar'),
    url(r'^exercicio/detalhar/(?P<pk>\d+)$', exercicio.detalhar, name='exercicio_detalhar'),
    url(r'^exercicio$', exercicio.listar, name='exercicio_listar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
