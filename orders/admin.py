from django.contrib import admin

from orders.models import CustomerOrderItem, CustomerOrder, SellerOrder, SellerOrderItem


class CustomerOrderItemsInline(admin.TabularInline):
    model = CustomerOrderItem
    min_num = 1
    extra = 1


class SellerOrderItemsInline(admin.TabularInline):
    model = SellerOrderItem
    min_num = 1
    extra = 1


class CustomerOrderAdmin(admin.ModelAdmin):
    fields = ('id', 'customer', 'user', 'cash', 'bank', 'credit', 'cuts', 'fines', 'perks', 'approved')
    list_display = ('customer', 'total', 'cash', 'bank', 'credit', 'approved')
    inlines = [CustomerOrderItemsInline]

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ['id', 'total']
        if obj and obj.pk:
            return ['id', 'total', 'approved', 'created_at']
        return ['id', 'approved', 'created_at', 'total']


class SellerOrderAdmin(admin.ModelAdmin):
    fields = ('seller', 'cash', 'bank', 'credit', 'approved')
    list_display = ('seller', 'total', 'cash', 'bank', 'credit', 'approved')
    inlines = [SellerOrderItemsInline]

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ['total']
        if obj and obj.pk:
            return ['total', 'approved', 'created_at']
        return ['approved', 'created_at', 'total']


admin.site.register(CustomerOrder, CustomerOrderAdmin)
admin.site.register(SellerOrder, SellerOrderAdmin)
