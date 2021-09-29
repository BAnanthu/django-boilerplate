from django.contrib import admin

# Register your models here.
from combine_multiple_model_rest.models import Model1, Model2

admin.site.register(Model1)
admin.site.register(Model2)