from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers

from .models import Persona


class PersonaSerializers(serializers.ModelSerializer):
    class Meta:
        model= Persona
        fields= '__all__'
        