from django.conf.urls import url

from .views import semilla_list, SemillaCreate, semillaUpdate, SemillaDelete

urlpatterns = [
    url(r'^$', semilla_list, name='list'),
    url(r'^inventario/$', SemillaCreate.as_view(), name='inventario'),
    url(r'^inventario/editar/(?P<id_semilla>\d+)$', semillaUpdate, name='inventario_editar'),
    url(r'^inventario/eliminar/(?P<pk>\d+)$', SemillaDelete.as_view(), name='inventario_eliminar'),
]
