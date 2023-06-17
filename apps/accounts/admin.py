from django.contrib import admin

from apps.accounts.models import Worker


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'inn', 'position')
