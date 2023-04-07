from rest_framework import serializers

from .models import Person, Species

class PersonSerializer(serializers.ModelSerializer):
   class Meta:
       model = Person
       fields = ('id','name', 'birth_year', 'eye_color', 'species')


class SpeciesSerializer(serializers.ModelSerializer):
   class Meta:
       model = Species
       fields = ('id','name', 'classification', 'language')