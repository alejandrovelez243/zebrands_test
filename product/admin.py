from django.contrib import admin

from product.models import Brand, Product

# Register your models here.


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "status", "creation_date", "updated_date")
    search_fields = ("name__icontains",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "sku",
        "name",
        "brand",
        "called",
        "status",
        "creation_date",
        "updated_date",
    )
    search_fields = ("sku__icontains", "name__icontains", "brand__name__icontains")
