from django.contrib import admin
from .models import Flat, Complaint, Owner
from django.contrib.auth.models import User
from django.db import models

class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town', 'owners_phonenumber', 'pure_phonenumber')
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['liked_by']

class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['user', 'flat']

class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['ownership']


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)