from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ["product"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "id", "first_name", "last_name", "email",
        "paid", "country", "city", "address",
        "postal_code", "created", "updated"
    ]

    list_display_links = ["first_name", "last_name", "email"]
    list_filter = ["paid", "country", "city", "created", "updated"]
    search_fields = ["first_name", "last_name",
                     "email", "address", "postal_code"]
    inlines = [OrderItemInline]