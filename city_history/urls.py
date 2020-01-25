# Django
from django.urls import path

from .views import CountryView, CountryNew, CountryEdit

urlpatterns = [
    path('countries/', CountryView.as_view(), name="country_list"),
    path('countries/new', CountryNew.as_view(), name="country_new"),
    path('countries/edit/<int:pk>', CountryEdit.as_view(), name="country_edit"),
]
