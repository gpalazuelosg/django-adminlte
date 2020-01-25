# Django
from django.db import models

# solution
from core_app.models import ModelClass

# Create your models here.

class Country(ModelClass):
    """ Country class entity describing required fields. Inherits from ModelClass. """
    
    name = models.CharField(
        max_length=100,
        help_text="Country name",
        unique=True
    )

    def __str__(self):
        return f"{self.name}"

    def save(self):
        self.name = self.name.upper()
        super(Country,self).save()

    class Meta:
        verbose_name_plural = "Countries"