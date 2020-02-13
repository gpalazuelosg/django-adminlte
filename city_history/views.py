# Django
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

# solution
from .models import Country, State, City
from .forms import CountryForm, StateForm, CityForm


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


class StateEdit(LoginRequiredMixin, generic.UpdateView):
    model = State
    template_name = "city_history/state_form.html"
    context_object_name = "obj"
    form_class = StateForm
    success_url = reverse_lazy("city_history:state_list")
    login_url = "core_app:login"

    def form_valid(self, form):
        form.instance.lastupdatedby = self.request.user.id
        return super().form_valid(form)

class StateDelete(LoginRequiredMixin, generic.DeleteView):
    model = State
    template_name = "city_history/state_delete.html"
    context_object_name = "obj"
    success_url = reverse_lazy("city_history:state_list")


class CityView(LoginRequiredMixin, generic.ListView):
    model = City
    template_name = "city_history/city_list.html"
    context_object_name = "obj"
    login_url = "core_app:login"

class CityNew(LoginRequiredMixin, generic.CreateView):
    model = City
    template_name = "city_history/city_form.html"
    context_object_name = "obj"
    form_class = CityForm
    success_url = reverse_lazy("city_history:city_list")
    login_url = "core_app:login"

    def form_valid(self, form):
        form.instance.createdby = self.request.user
        return super().form_valid(form)

class CityEdit(LoginRequiredMixin, generic.UpdateView):
    model = City
    template_name = "city_history/city_form.html"
    context_object_name = "obj"
    form_class = CityForm
    success_url = reverse_lazy("city_history:city_list")
    login_url = "core_app:login"

    def form_valid(self, form):
        form.instance.lastupdatedby = self.request.user.id
        return super().form_valid(form)

# class CityDelete(LoginRequiredMixin, generic.DeleteView):
#     model = City
#     template_name = "city_history/city_delete.html"
#     context_object_name = "obj"
#     success_url = reverse_lazy("city_history:city_list")

def city_inactivate(request, id):
    city = City.objects.filter(pk=id).first()
    context = {}
    template_name = "city_history/city_delete.html"

    if not city:
        return redirect("city_history:city_list")
    
    if request.method=="GET":
        context= {"obj":city}
    
    if request.method=="POST":
        city.active = False
        city.save()
        return redirect("city_history:city_list")
    
    return render(request, template_name, context)
