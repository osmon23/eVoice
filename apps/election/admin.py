from django.contrib import admin
from .models import Election, ElectionType

admin.site.register(Election)
admin.site.register(ElectionType)
