# Django
from django.shortcuts import render
from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin

# solution
from .models import Country

# Create your views here.
class CountryView(LoginRequiredMixin, generic.ListView):
    model = Country
    template_name = "city_history/country_list.html"
    context_object_name = "obj"
    login_url = "core_app:login"
