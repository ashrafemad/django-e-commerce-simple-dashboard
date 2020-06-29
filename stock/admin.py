from django.contrib import admin
from stock.models import Category, Product, Attribute, AttributeValue


class ProductAttributesInline(admin.TabularInline):
    model = Product.attributes.through
    verbose_name = "Attribute"
    verbose_name_plural = "Attributes"


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'cost_price', 'quantity', 'product_attributes')
    exclude = ('attributes',)
    inlines = (ProductAttributesInline,)

    def product_attributes(self, obj):
        return ','.join([str(item) for item in obj.attributes.all()])
    product_attributes.short_description = 'Attributes'


class ProductAttributeAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Attribute, ProductAttributeAdmin)
admin.site.register(AttributeValue, ProductAttributeAdmin)
