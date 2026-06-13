from django.contrib import admin
from .models import Medicine, Order


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        'full_name',
        'mobile_number',
        'medicine',
        'quantity',
        'city',
        'status',
        'created_at',
    )

    list_filter = (
        'status',
        'medicine',
        'city',
        'created_at',
    )

    search_fields = (
        'full_name',
        'mobile_number',
        'city',
    )

    ordering = ('-created_at',)

    list_editable = ('status',)