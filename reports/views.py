from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView

from customers.models import Customer, Seller
from expenses.models import Revenue, Expense, InsurancePrimary
from orders.models import CustomerOrder, SellerOrder
from settings.models import StartBalance


class ReportView(TemplateView):
    template_name = 'reports/index.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_superuser:
            return redirect('/')
        return super().dispatch(request, args, kwargs)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()
        month = self.request.GET.get('month', 12)
        year = self.request.GET.get('year', 2019)

        ctx['total_selling'] = sum([item.total() for item in CustomerOrder.objects.filter(approved=True, created_at__month=month, created_at__year=year)])

        ctx['total_buying'] = sum([item.total() for item in SellerOrder.objects.filter(approved=True, created_at__month=month, created_at__year=year)])

        ctx['total_customer_payments'] = sum([item.total_payments(month, year) for item in Customer.objects.all()])
        ctx['total_seller_payments'] = sum([item.total_payments(month, year) for item in Seller.objects.all()])

        ctx['total_revenues'] = sum([item.value for item in Revenue.objects.filter(created_at__month=month, created_at__year=year)])
        ctx['total_expenses'] = sum([item.value for item in Expense.objects.filter(created_at__month=month, created_at__year=year)])

        ctx['total_selling_cost'] = sum([item.total_cost() for item in CustomerOrder.objects.filter(approved=True, created_at__month=month, created_at__year=year)])

        ctx['insurance_primary'] = sum([item.value for item in InsurancePrimary.objects.filter(refunded=True)])

        ctx['cash_balance'] = sum([item.total_cash_payments(month, year) for item in Customer.objects.all()]) + StartBalance.get_solo().cash
        ctx['bank_balance'] = sum(
            [item.total_bank_payments(month, year) for item in Customer.objects.all()]) + StartBalance.get_solo().bank
        return ctx
