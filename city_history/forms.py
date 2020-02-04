from django import forms

# my models
from .models import Country, State

class CountryForm(forms.ModelForm):

    class Meta:
        model = Country
        fields = ["name", "active"]
        labels = {
            "name": "Country Name",
            "active": "Is Active?"
        }
        widget = { 
            "name": forms.TextInput 
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                "class": "form-control"
            })


class StateForm(forms.ModelForm):
    country = forms.ModelChoiceField(
        queryset = Country.objects.filter(active=True)
        .order_by("name")
    )
    class Meta:
        model = State
        fields = ["country", "name", "active"]
        labels = {
            "name": "State Name",
            "active": "Is Active?"
        }
        widget = { 
            "name": forms.TextInput 
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                "class": "form-control"
            })

        self.fields["country"].empty_label = "Select country"

    

