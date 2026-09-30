from django.contrib import admin
from .models import Car, Contact, Order


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("car_id", "car_name", "category", "seats", "transmission", "fuel_type", "price", "is_available")
    search_fields = ("car_name", "car_desc")
    list_filter = ("category", "transmission", "fuel_type", "is_available")
    list_editable = ("price", "is_available")
    ordering = ("car_id",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("reference", "name", "user", "cars", "pickup_date", "return_date", "total_rent", "status")
    search_fields = ("name", "email", "cars", "phone")
    list_filter = ("status", "cars", "pickup_date")
    readonly_fields = ("created_at", "total_rent", "pickup_date", "return_date")


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone_number", "created_at")
    search_fields = ("name", "email", "message_text")
    readonly_fields = ("created_at",)
