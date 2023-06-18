from django.contrib import admin
from .models import Election, ElectionType


@admin.register(Election)
class ElectionAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'image',
        'description',
        'start_date',
        'end_date',
        'election_type',
        'is_active',
    )


admin.site.register(ElectionType)
