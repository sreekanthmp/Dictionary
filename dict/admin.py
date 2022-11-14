from django.contrib import admin

# Register your models here.

from . models import Dictionary
from . models import Dict

admin.site.register(Dictionary)
admin.site.register(Dict)

