from django.db import models

DEVICE_CATEGORY_CHOICES = (
    ("", ""),
    ("Smartphone", "Smartphone"),
    ("Feature Phone", "Feature Phone"),
    ("Connect Device", "Connect Device"),
    ("Tablet", "Tablet"),
    ("Case", "Case"),
)


class PhoneCatalog(models.Model):
    uid = models.CharField(max_length=255, null=False)
    phone_combined = models.CharField(max_length=255, blank=True, default="")
    admin_slug = models.CharField(max_length=255, blank=True, default="")
    product_id = models.CharField(max_length=255, blank=True, default="", unique=True)
    manufacturer = models.CharField(max_length=255, blank=True, default="")
    device_name = models.CharField(max_length=255, blank=True, default="")
    device_model = models.CharField(max_length=255, blank=True, default="")
    carrier = models.CharField(max_length=255, blank=True, default="")
    quote_new = models.CharField(max_length=255, blank=True, default="")
    quote_working = models.CharField(max_length=255, blank=True, default="")
    quote_broken = models.CharField(max_length=255, blank=True, default="")
    extra_csv_cols = models.TextField()
    device_category = models.CharField(
        max_length=255, blank=True, default="", choices=DEVICE_CATEGORY_CHOICES
    )
    requires_managers_approval = models.BooleanField(default=False)
    commission_eligible = models.BooleanField(default=False)
    commission_eligible_empty = models.BooleanField(default=False, editable=False)
    show_on_quote_pricing_tool = models.BooleanField(default=False)
    show_on_sales_order_pricing_tool = models.BooleanField(default=False)
    sales_order_used_b_stock_pricing = models.CharField(
        max_length=255, blank=True, default=""
    )

    fmv_ftw = models.CharField(max_length=255, blank=True, default="")
    fmv_pgl = models.CharField(max_length=255, blank=True, default="")
    fmv_pbl = models.CharField(max_length=255, blank=True, default="")
    fmv_np = models.CharField(max_length=255, blank=True, default="")
    fmv_pgl_icloud = models.CharField(max_length=255, blank=True, default="")
    fmv_pbl_icloud = models.CharField(max_length=255, blank=True, default="")

    active = models.BooleanField(default=True, editable=False)

    class Meta:
        ordering = ["manufacturer", "device_name", "device_model"]
        verbose_name = "Catalog Phone"
        verbose_name_plural = "Catalog Phones"


class PhoneCatalogSOPricing(PhoneCatalog):
    class Meta:
        proxy = True
