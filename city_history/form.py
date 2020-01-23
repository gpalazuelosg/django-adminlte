from django import forms

# my models
from .models import Country

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
    