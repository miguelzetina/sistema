import os

from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve

from . import settings

handler404 = 'sistema.views.error404'
handler403 = 'sistema.views.error403'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include("inventario.urls", namespace="inventario")),
]

if settings.DEBUG404:
    urlpatterns += (
        url(r'^static/(?P<path>.*)', serve,
            {
                'document_root': os.path.join(os.path.join(os.path.dirname(settings.BASE_DIR), 'static_cdn'))
            }
            ),
    )