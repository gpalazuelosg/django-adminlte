# Django
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

# solution
from .models import Country, State
from .forms import CountryForm, StateForm


# Create your views here.
class CountryView(LoginRequiredMixin, generic.ListView):
    model = Country
    template_name = "city_history/country_list.html"
    context_object_name = "obj"
    login_url = "core_app:login"

class CountryNew(LoginRequiredMixin, generic.CreateView):
    model = Country
    template_name = "city_history/country_form.html"
    context_object_name = "obj"
    form_class = CountryForm
    success_url = reverse_lazy("city_history:country_list")
    login_url = "core_app:login"

    def form_valid(self, form):
        form.instance.createdby = self.request.user
        return super().form_valid(form)

class CountryEdit(LoginRequiredMixin, generic.UpdateView):
    model = Country
    template_name = "city_history/country_form.html"
    context_object_name = "obj"
    form_class = CountryForm
    success_url = reverse_lazy("city_history:country_list")
    login_url = "core_app:login"

    def form_valid(self, form):
        form.instance.lastupdatedby = self.request.user.id
        return super().form_valid(form)

class CountryDelete(LoginRequiredMixin, generic.DeleteView):
    model = Country
    template_name = "city_history/country_delete.html"
    context_object_name = "obj"
    success_url = reverse_lazy("city_history:country_list")


class StateView(LoginRequiredMixin, generic.ListView):
    model = State
    template_name = "city_history/state_list.html"
    context_object_name = "obj"
    login_url = "core_app:login"


class StateNew(LoginRequiredMixin, generic.CreateView):
    model = State
    template_name = "city_history/state_form.html"
    context_object_name = "obj"
    form_class = StateForm
    success_url = reverse_lazy("city_history:state_list")
    login_url = "core_app:login"

    def form_valid(self, form):
        form.instance.createdby = self.request.user
        return super().form_valid(form)