from django.contrib import admin

from main_app.models.models import (
    Laboratories
)

@admin.register(Laboratories)
class LaboratoriesAdmin(admin.ModelAdmin):
    """FeatureCompany model admin."""

    list_display = (
        'name',
        'description',
    )
    search_fields = ('name',)
    list_filter = ('name',)
