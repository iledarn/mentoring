from django.contrib import admin

from gbwphone.models import PhoneCatalog, PhoneCatalogSOPricing


@admin.register(PhoneCatalog)
class PhoneCatalogAdmin(admin.ModelAdmin):
    enable_nav_sidebar = False
    list_display = [
        "view_id",
        "view_admin_slug",
        "active",
    ]

    def view_admin_slug(self, obj):
        return obj.admin_slug

    view_admin_slug.short_description = "Name"

    def view_id(self, obj):
        return obj.id

    view_id.short_description = "Product ID"


@admin.register(PhoneCatalogSOPricing)
class PhoneCatalogSOPricingAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "view_admin_slug",
        "show_on_sales_order_pricing_tool",
        "sales_order_used_b_stock_pricing",
    ]
    list_editable = [
        "show_on_sales_order_pricing_tool",
        "sales_order_used_b_stock_pricing",
    ]
    def view_admin_slug(self, obj):
        return obj.admin_slug
    view_admin_slug.short_description = "Name"

