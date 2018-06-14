from django.contrib import admin
from .models import Interaction

# Register your models here.
admin.register(Interaction)(admin.ModelAdmin)
