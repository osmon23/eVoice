from django.contrib import admin
from models import ElectionType, Election, Candidate

admin.site.register(ElectionType)
admin.site.register(Election)
admin.site.register(Candidate)
