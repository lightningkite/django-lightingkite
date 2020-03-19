from django.urls import path

from .views import StripeView

urlpatterns = [
    path('', StripeView, name='stripe'),
]
