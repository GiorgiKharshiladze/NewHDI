from django.contrib import admin
from dataMining.models import Indicator

# Register your models here.

admin.register(Indicator)(admin.ModelAdmin)

# admin.register(one, two, three)(admin.ModelAdmin)
