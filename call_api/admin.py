from django.contrib import admin

# Register your models here.
from .models import Species,Person

# Register your models here.
admin.site.register(Species)
admin.site.register(Person)
