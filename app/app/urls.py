from django.urls import path, include
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import re_path as url

router = routers.DefaultRouter()

schema_view = get_schema_view(
    openapi.Info(
        title="API Example",
        default_version='v1.0',
        description="<h4>Docs for Example API</h4>",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('api.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    url(r'^static/(?P<path>.*)$', serve, {'document_root':settings.STATIC_ROOT}),
    url(r'^public/(?P<path>.*)$', serve, {'document_root':settings.PUBLIC_ROOT}),
]
