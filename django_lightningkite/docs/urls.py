from django.urls import path
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

from rest_framework.schemas import get_schema_view

from . import settings

schema_args = {
    'title': settings.DOCS_TITLE,
    'description': settings.DOCS_DESCRIPTION,
    'version': settings.DOCS_VERSION,
}

if settings.PUBLIC_DOCS:
    schema_args['public'] = True
    schema_args['permission_classes'] = []

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='docs-redoc')),
    path('schema', get_schema_view(**schema_args), name='docs-schema'),
    path('redoc/', TemplateView.as_view(
        template_name='redoc.html',
        extra_context={'schema_url': 'docs-schema'}
    ), name='docs-redoc'),

    path('swagger/', TemplateView.as_view(
        template_name='swagger.html',
        extra_context={'schema_url': 'docs-schema'}
    ), name='docs-swagger'),
]
