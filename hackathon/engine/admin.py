from django.contrib import admin

# Register your models here.
from engine.models import Found,Lost

admin.site.register(Found)
admin.site.register(Lost)