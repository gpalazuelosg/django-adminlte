# Django
from django.urls import path

from .views import CountryView

urlpatterns = [
    path('countries/', CountryView.as_view(), name="country_list"),
]
