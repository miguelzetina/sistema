from django.conf.urls import url

from .views import semilla_list, SemillaCreate, semillaUpdate, SemillaDelete

urlpatterns = [
    url(r'^$', semilla_list, name='list'),
    url(r'^semilla/$', SemillaCreate.as_view(), name='semilla'),
    url(r'^semilla/editar/(?P<id_semilla>\d+)$', semillaUpdate, name='semilla_editar'),
    url(r'^semilla/eliminar/(?P<pk>\d+)$', SemillaDelete.as_view(), name='semilla_eliminar'),
]
