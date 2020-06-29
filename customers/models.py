from django.db import models
from django.utils.timezone import localtime, now
from django.utils.translation import gettext_lazy as _


class BaseCustomerSeller(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('Name'))
    address = models.CharField(max_length=254, verbose_name=_('Address'))
    phone_number = models.CharField(max_length=20, verbose_name=_('Phone number'))
    email = models.EmailField(null=True, blank=True, verbose_name=_('Email'))
    company_name = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('Company name'))
    payment_info = models.TextField(help_text=_('bank account number, E-wallet, ...etc'), null=True, blank=True, verbose_name=_('Payment info'))
    join_date = models.DateField(verbose_name=_('Join date'))

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Customer(BaseCustomerSeller):
    CUSTOMER_TYPE_CHOICES = (
        ('New', 'New'),
        ('Current', 'Current'),
        ('Expected', 'Expected'),
        ('Facebook', 'Facebook'),
    )
    customer_type = models.CharField(max_length=50, choices=CUSTOMER_TYPE_CHOICES, default='Current', verbose_name=_('Customer type'))
    person_name = models.CharField(max_length=200, default='-', verbose_name=_('Person name'))
    person_job = models.CharField(max_length=200, default='-', verbose_name=_('Person job'))

    def alarm(self):
        last_order = self.orders.filter(approved=True).last()
        if last_order:
            delta = localtime(now()) - localtime(last_order.created_at)
            if delta and delta.days >= 334:
                return True
        return False
    alarm.boolean = True
    alarm.short_description = _('Alarm')

    def total_purchases(self, month=None, year=None):
        if month and year:
            return sum([order.total() for order in self.orders.filter(approved=True, created_at__month=month, created_at__year=year)])
        return sum([order.total() for order in self.orders.filter(approved=True)])
    total_purchases.short_description = _('Total Purchases')

    def total_payments(self, month=None, year=None):
        if month and year:
            total_direct_payments = sum([item.net_value() for item in self.customer_payments.filter(approved=True,created_at__month=month, created_at__year=year)])
            total_order_cash_payment = sum([item.cash + item.bank for item in self.orders.filter(approved=True, created_at__month=month, created_at__year=year)])
        else:
            total_direct_payments = sum([item.net_value() for item in self.customer_payments.filter(approved=True)])
            total_order_cash_payment = sum([item.cash + item.bank for item in self.orders.filter(approved=True)])
        return total_direct_payments + total_order_cash_payment

    total_payments.short_description = _('Total payments')

    def total_cash_payments(self, month=None, year=None):
        if month and year:
            total_direct_payments = sum(
                [item.net_value() for item in self.customer_payments.filter(payment_method='Cash', approved=True, created_at__month=month, created_at__year=year)])
            total_order_cash_payment = sum([item.cash for item in self.orders.filter(approved=True, created_at__month=month, created_at__year=year)])
        else:
            total_direct_payments = sum([item.net_value() for item in self.customer_payments.filter(payment_method='Cash',approved=True)])
            total_order_cash_payment = sum([item.cash for item in self.orders.filter(approved=True)])
        return total_direct_payments + total_order_cash_payment

    total_cash_payments.short_description = _('Total cash payments')

    def total_bank_payments(self, month=None, year=None):
        if month and year:
            total_direct_payments = sum(
                [item.net_value() for item in self.customer_payments.filter(payment_method='Bank', approved=True, created_at__month=month, created_at__year=year)])
            total_order_cash_payment = sum([item.bank for item in self.orders.filter(approved=True, created_at__month=month, created_at__year=year)])
        else:
            total_direct_payments = sum(
                [item.net_value() for item in self.customer_payments.filter(payment_method='Bank', approved=True)])
            total_order_cash_payment = sum([item.bank for item in self.orders.filter(approved=True)])
        return total_direct_payments + total_order_cash_payment

    total_bank_payments.short_description = _('Total bank payments')

    def balance(self):
        return self.total_purchases() - self.total_payments()
    balance.short_description = _('Balance')

    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')


class Seller(BaseCustomerSeller):

    def total_purchases(self):
        return sum([order.total() for order in self.orders.filter(approved=True)])

    total_purchases.short_description = _('Total Purchases')

    def total_payments(self, month=None, year=None):
        if month and year:
            total_direct_payments = sum([item.net_value() for item in self.seller_payments.filter(approved=True, created_at__month=month, created_at__year=year)])
            total_order_cash_payment = sum([item.cash + item.bank for item in self.orders.filter(approved=True, created_at__month=month, created_at__year=year)])
        else:
            total_direct_payments = sum([item.net_value() for item in self.seller_payments.filter(approved=True)])
            total_order_cash_payment = sum([item.cash + item.bank for item in self.orders.filter(approved=True)])
        return total_direct_payments + total_order_cash_payment

    total_payments.short_description = _('Total payments')

    def total_cash_payments(self, month=None, year=None):
        if month and year:
            total_direct_payments = sum(
                [item.net_value() for item in self.seller_payments.filter(payment_method='Cash', approved=True, created_at__month=month, created_at__year=year)])
            total_order_cash_payment = sum([item.cash for item in self.orders.filter(approved=True, created_at__month=month, created_at__year=year)])
        else:
            total_direct_payments = sum(
                [item.net_value() for item in self.seller_payments.filter(payment_method='Cash', approved=True)])
            total_order_cash_payment = sum([item.cash for item in self.orders.filter(approved=True)])
        return total_direct_payments + total_order_cash_payment

    total_cash_payments.short_description = _('Total cash payments')

    def total_bank_payments(self, month=None, year=None):
        if month and year:
            total_direct_payments = sum(
                [item.net_value() for item in self.seller_payments.filter(payment_method='Bank', approved=True, created_at__month=month, created_at__year=year)])
            total_order_cash_payment = sum([item.bank for item in self.orders.filter(approved=True, created_at__month=month, created_at__year=year)])
        else:
            total_direct_payments = sum(
                [item.net_value() for item in self.seller_payments.filter(payment_method='Bank', approved=True)])
            total_order_cash_payment = sum([item.bank for item in self.orders.filter(approved=True)])
        return total_direct_payments + total_order_cash_payment

    total_bank_payments.short_description = _('Total bank payments')

    def balance(self):
        return self.total_purchases() - self.total_payments()

    balance.short_description = _('Balance')

    class Meta:
        verbose_name = _('Seller')
        verbose_name_plural = _('Sellers')


class CustomerPayment(models.Model):
    PAYMENT_METHOD_CHOICES = (
        ('Cash', 'Cash'),
        ('Bank', 'Bank'),
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_payments', verbose_name=_('Customer'))
    payment_method = models.CharField(max_length=100, choices=PAYMENT_METHOD_CHOICES, verbose_name=_('Payment method'))
    value = models.FloatField(verbose_name=_('Value'))
    order = models.ForeignKey('orders.CustomerOrder', on_delete=models.SET_NULL, null=True, verbose_name=_('Order'))
    cuts = models.FloatField(verbose_name=_('Cuts'), default=0)
    fines = models.FloatField(verbose_name=_('Fines'), default=0)
    perks = models.FloatField(verbose_name=_('Perks'), default=0)
    approved = models.BooleanField(default=False, verbose_name=_('Approved'))
    created_at = models.DateTimeField(auto_now=True, verbose_name=_('Created at'))

    def __str__(self):
        return f'{self.customer}-{self.value}'

    def net_value(self):
        if self.pk:
            return self.value - (self.cuts + self.fines + self.perks)
        return 0

    class Meta:
        verbose_name = _('Customer payment')
        verbose_name_plural = _('Customer payments')


class SellerPayment(models.Model):
    PAYMENT_METHOD_CHOICES = (
        ('Cash', 'Cash'),
        ('Bank', 'Bank'),
    )
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='seller_payments', verbose_name=_('Seller'), null=True)
    payment_method = models.CharField(max_length=100, choices=PAYMENT_METHOD_CHOICES, verbose_name=_('Payment method'))
    value = models.FloatField(verbose_name=_('Value'))
    cuts = models.FloatField(verbose_name=_('Cuts'), default=0)
    fines = models.FloatField(verbose_name=_('Fines'), default=0)
    perks = models.FloatField(verbose_name=_('Perks'), default=0)
    approved = models.BooleanField(default=False, verbose_name=_('Approved'))
    created_at = models.DateTimeField(auto_now=True, verbose_name=_('Created at'))

    def __str__(self):
        return f'{self.seller}-{self.value}'

    def net_value(self):
        if self.pk:
            return self.value - (self.cuts + self.fines + self.perks)
        return 0

    class Meta:
        verbose_name = _('Seller payment')
        verbose_name_plural = _('Seller payments')


class CustomerWithBalanceManager(models.Manager):
    def get_queryset(self):
        customers = []
        queryset = super(CustomerWithBalanceManager, self).get_queryset()
        for customer in queryset:
            if customer.balance() > 0:
                customers.append(customer.id)
        return queryset.filter(id__in=customers)


class CustomerWithBalance(Customer):

    objects = CustomerWithBalanceManager()

    class Meta:
        proxy = True
        verbose_name = 'مدين'
        verbose_name_plural = 'مدينين'