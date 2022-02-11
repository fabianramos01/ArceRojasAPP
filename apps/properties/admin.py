from django.contrib.admin import ModelAdmin, register

from apps.properties.models import Property, Owner

@register(Property)
class PropertyAdmin(ModelAdmin):
    list_display = ('registration_number', 'cadastral_id', 'address', 'name', 'type')
    ordering = ('-registration_number',)

@register(Owner)
class OwnerAdmin(ModelAdmin):
    list_display = ('identification', 'name', 'type')
    ordering = ('-name',)
