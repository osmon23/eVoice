from django.contrib import admin
from .models import Election, ElectionType, ReferendumType


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


@admin.register(ReferendumType)
class ReferendumTypeAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'voice_positive',
        'voice_negative',
    )


admin.site.register(ElectionType)
