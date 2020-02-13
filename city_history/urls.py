# Django
from django.urls import path

from .views import CountryView, CountryNew, CountryEdit, CountryDelete, \
    StateView, StateNew, StateEdit, StateDelete, \
    CityView, CityNew, CityEdit, city_inactivate

urlpatterns = [
    path('countries/', CountryView.as_view(), name="country_list"),
    path('countries/new', CountryNew.as_view(), name="country_new"),
    path('countries/edit/<int:pk>', CountryEdit.as_view(), name="country_edit"),
    path('countries/delete/<int:pk>', CountryDelete.as_view(), name="country_delete"),

    path('states/', StateView.as_view(), name="state_list"),
    path('states/new', StateNew.as_view(), name="state_new"),
    path('states/edit/<int:pk>', StateEdit.as_view(), name="state_edit"),
    path('states/delete/<int:pk>', StateDelete.as_view(), name="state_delete"),

    path('cities/', CityView.as_view(), name="city_list"),
    path('cities/new', CityNew.as_view(), name="city_new"),
    path('cities/edit/<int:pk>', CityEdit.as_view(), name="city_edit"),
    path("cities/inactivate/<int:id>", city_inactivate, name="city_delete"),

]
