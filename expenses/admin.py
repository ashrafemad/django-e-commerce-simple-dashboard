from django.contrib import admin

from expenses.models import Expense, Revenue, InsurancePrimary, InsuranceFinal


class BaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'created_at', 'approved')
    list_filter = ('approved',)

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ['created_at']
        if obj and obj.pk:
            return ['name', 'value', 'approved', 'created_at']
        return ['approved', 'created_at']


class InsurancePrimaryAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'refunded', 'refunded_by', 'created_at')
    readonly_fields = ('created_at',)


class InsuranceFinalAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'refund_date', 'created_at')
    readonly_fields = ('created_at',)


admin.site.register(Expense, BaseAdmin)
admin.site.register(Revenue, BaseAdmin)
admin.site.register(InsurancePrimary, InsurancePrimaryAdmin)
admin.site.register(InsuranceFinal, InsuranceFinalAdmin)
