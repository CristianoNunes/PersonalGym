from django.conf.urls import url
from .views import aluno
from .views import index


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^aluno/adicionar$', aluno.adicionar, name='aluno_adicionar'),
    url(r'^aluno/editar/(?P<pk>\d+)$', aluno.editar, name='aluno_editar'),
    url(r'^aluno/apagar/(?P<pk>\d+)$', aluno.apagar, name='aluno_apagar'),
    url(r'^aluno/detalhar/(?P<pk>\d+)$', aluno.detalhar, name='aluno_detalhar'),
    url(r'^aluno$', aluno.listar, name='aluno_listar'),
]
