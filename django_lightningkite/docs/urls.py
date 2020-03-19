from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view

from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='docs-redoc')),

    path('schema', get_schema_view(
        title="Your Project",
        description="API for all things …",
        version="0.0.0"
    ), name='docs-schema'),

    path('redoc/', TemplateView.as_view(
        template_name='redoc.html',
        extra_context={'schema_url': 'docs-schema'}
    ), name='docs-redoc'),

    path('swagger/', TemplateView.as_view(
        template_name='swagger.html',
        extra_context={'schema_url': 'docs-schema'}
    ), name='docs-swagger'),
]

