from django.contrib import admin

from .models import Referendum, Citizen


@admin.register(Referendum)
class Referendum(admin.ModelAdmin):
    # list_display = (
    #     'INN',
    #     'biometry',
    #     'choice',
    #     'election',
    # )
    readonly_fields = (
        'INN',
        'biometry',
        'choice',
        'election',
    )


@admin.register(Citizen)
class Citizen(admin.ModelAdmin):
    # list_display = (
    #     'phone_number',
    #     'email',
    #     'video',
    #     'candidate',
    #     'status',
    # )
    readonly_fields = (
        'phone_number',
        'email',
        'video',
        'candidate',
        'INN',
        'biometry',
        'choice',
        'photo',
    )
