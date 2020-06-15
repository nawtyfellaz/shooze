from django.contrib import admin
from shooze.product.models import Product, Seller, Brand, Images

# Register your models here.
class StoreAdmin(admin.ModelAdmin):
    list_display = ['oname', 'title', 'active']
    list_filter = ['active']
    list_editable = ['title', 'active']
    ordering = ['active', '-title']
    search_fields = ['oname', 'title']

    def oname(self, instance):
        return instance.owner.user.username

    class Meta:
        model = Seller

admin.site.register(Seller, StoreAdmin)

class ProductImagesInline(admin.StackedInline):
    model = Images

class ProductAdmin(admin.ModelAdmin):
    list_display = ['sname', 'title', 'maf_date', 'digital', 'featured', 'instock']
    list_filter = ['instock', 'featured', 'maf_date', 'digital']
    list_editable = ['featured', 'maf_date', 'digital', 'title']
    ordering = ['maf_date', '-title', 'instock']
    search_fields = ['sname', 'title', 'description', 'maf_date']
    inlines = [ProductImagesInline]

    def sname(self, instance):
        return instance.store.title

    class Meta:
        model = Product
        
admin.site.register(Product, ProductAdmin)


admin.site.register(Brand)
