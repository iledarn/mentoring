from django.contrib import admin

from gbwphone.models import PhoneCatalog


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
