from django.contrib import admin
from customers.models import Customer, Seller, CustomerPayment, SellerPayment, CustomerWithBalance


class CustomerPaymentAdmin(admin.ModelAdmin):
    list_filter = ('customer', 'payment_method')
    list_display = ('customer', 'payment_method', 'value', 'order', 'approved')

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        if obj and obj.pk:
            return['customer', 'payment_method', 'value', 'cuts', 'fines', 'perks', 'approved',
                  'created_at']
        return ['approved']


class SellerPaymentAdmin(admin.ModelAdmin):
    list_filter = ('seller', 'payment_method')
    list_display = ('seller', 'payment_method', 'value', 'approved')

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        if obj and obj.pk:
            return['customer', 'payment_method', 'value', 'cuts', 'fines', 'perks', 'approved',
                   'created_at']
        return ['approved']


class CustomerAdmin(admin.ModelAdmin):
    list_filter = ('customer_type', )
    list_display = ('name',
                    'customer_type',
                    'phone_number',
                    'company_name',
                    'total_purchases',
                    'balance',
                    'join_date', 'alarm')
    readonly_fields = ('total_purchases', 'total_payments', 'total_cash_payments', 'total_bank_payments', 'balance')


class SellerAdmin(CustomerAdmin):
    inlines = []
    list_filter = ()
    list_display = ('name',
                    'phone_number',
                    'company_name',
                    'balance',
                    'join_date')
    readonly_fields = ('balance', )


class CustomerWithBalanceAdmin(admin.ModelAdmin):
    list_display = ('name', 'net_balance',)
    list_display_links = None

    def net_balance(self, obj):
        return obj.balance()
    net_balance.short_description = 'مديونية'

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False


admin.site.register(Customer, CustomerAdmin)
admin.site.register(CustomerPayment, CustomerPaymentAdmin)
admin.site.register(SellerPayment, SellerPaymentAdmin)
admin.site.register(Seller, SellerAdmin)
admin.site.register(CustomerWithBalance, CustomerWithBalanceAdmin)
