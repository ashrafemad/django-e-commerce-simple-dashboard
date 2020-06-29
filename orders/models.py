from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db import models

from customers.models import Customer, Seller
from stock.models import Product


class AbstractOrder(models.Model):
    cash = models.FloatField(verbose_name=_('Cash'), default=0)
    bank = models.FloatField(verbose_name=_('Bank'), default=0)
    credit = models.FloatField(verbose_name=_('Credit'), default=0)
    cuts = models.FloatField(verbose_name=_('Cuts'), default=0)
    fines = models.FloatField(verbose_name=_('Fines'), default=0)
    perks = models.FloatField(verbose_name=_('Perks'), default=0)
    approved = models.BooleanField(default=False, verbose_name=_('Approved'), )
    created_at = models.DateTimeField(auto_now=True, verbose_name=_('Created at'), )

    def total(self):
        total_cuts = self.cuts + self.fines + self.perks
        total_net = sum([item.total() for item in self.order_items.all()])
        return total_net - total_cuts
    total.short_description = _('Total')

    def total_cost(self):
        return sum([item.total_cost() for item in self.order_items.all()])

    def __str__(self):
        return f'{self.id}-{self.total()}'

    class Meta:
        abstract = True


class CustomerOrder(AbstractOrder):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders', verbose_name=_('Customer'),)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name=_('Sales Representative'))

    class Meta:
        verbose_name = _('Customer Order')
        verbose_name_plural = _('Customer Orders')


class SellerOrder(AbstractOrder):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, verbose_name=_('Seller'), related_name='orders')

    class Meta:
        verbose_name = _('Seller Order')
        verbose_name_plural = _('Seller Orders')


class AbstractOrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('Product'))
    quantity = models.IntegerField(verbose_name=_('Quantity'))
    price = models.FloatField(help_text=_('Price of single piece of quantity'), verbose_name=_('Price'))

    def total(self):
        return self.quantity * self.price

    total.short_description = _('Total')

    def total_cost(self):
        return self.product.cost_price * self.quantity

    class Meta:
        abstract = True
        verbose_name = _('Order item')
        verbose_name_plural = _('Order items')


class CustomerOrderItem(AbstractOrderItem):
    order = models.ForeignKey(CustomerOrder, on_delete=models.CASCADE, related_name='order_items', verbose_name=_('Order'))


class SellerOrderItem(AbstractOrderItem):
    order = models.ForeignKey(SellerOrder, on_delete=models.CASCADE, related_name='order_items',
                              verbose_name=_('Order'))

