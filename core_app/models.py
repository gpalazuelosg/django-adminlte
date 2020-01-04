from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class ModelClass(models.Model):
    """Base class for my solution for common fields."""

    active = models.BooleanField(default=True)
    createdon = models.DateTimeField(auto_now_add=True)
    createdby = models.ForeignKey(User, on_delete=models.CASCADE)
    lastupdatedon = models.DateTimeField(auto_now=True)
    lastupdatedby = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract = True
