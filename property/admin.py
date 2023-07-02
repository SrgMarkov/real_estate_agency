from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnersInstanceInline(admin.TabularInline):
    model = Flat.owners.through
    raw_id_fields = ('owner',)


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address']
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'floor', 'rooms_number', 'has_balcony')
    raw_id_fields = ('liked_by',)
    inlines = [
        OwnersInstanceInline,
    ]


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_flat')
    raw_id_fields = ('flat',)


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('complaining_user', 'complain_flat')


admin.site.register(Flat, FlatAdmin)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(Complaint, ComplaintAdmin)