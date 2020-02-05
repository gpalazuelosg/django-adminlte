# Django
from django.urls import path

from .views import CountryView, CountryNew, CountryEdit, CountryDelete, \
    StateView, StateNew, StateEdit

urlpatterns = [
    path('countries/', CountryView.as_view(), name="country_list"),
    path('countries/new', CountryNew.as_view(), name="country_new"),
    path('countries/edit/<int:pk>', CountryEdit.as_view(), name="country_edit"),
    path('countries/delete/<int:pk>', CountryDelete.as_view(), name="country_delete"),

    path('states/', StateView.as_view(), name="state_list"),
    path('states/new', StateNew.as_view(), name="state_new"),
    path('states/edit/<int:pk>', StateEdit.as_view(), name="state_edit"),

]
