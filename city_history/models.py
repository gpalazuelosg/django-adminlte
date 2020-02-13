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


class State(ModelClass):
    """ State class for this solution which is linked to one Country entity. Inherits from ModelClass. """
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(
        max_length= 100,
        help_text= "State name",
        blank= False,
        null= False
    )

    def __str__(self, *args, **kwargs):
        return f"{self.country.name}:{self.name}"
    
    def save(self):
        self.name = self.name.upper()
        super(State,self).save()

    class Meta:
        verbose_name_plural = "States"

        # es un unique compuesto
        unique_together = ("country", "name")

class City(ModelClass):
    """ City class for this solution which is linked to one State entity. Inherits from ModelClass."""
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=100,
        help_text="City name",
        blank= False,
        null=False
    )

    def __str__(self, *args, **kwargs):
        return f"{self.state.name}:{self.name}"
    
    def save(self):
        self.name = self.name.upper()
        super(City,self).save()
    
    class Meta:
        verbose_name_plural = "Cities"

        # es un unique compuesto
        unique_together = ("state", "name")
    