from django.db import models
from django.utils.translation import gettext_lazy as _


class Expense(models.Model):
    name = models.CharField(max_length=150, verbose_name=_('Name'))
    value = models.FloatField(verbose_name=_('Value'))
    approved = models.BooleanField(default=False, verbose_name=_('Approved'))
    created_at = models.DateTimeField(auto_now=True, verbose_name=_('Created at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Expense')
        verbose_name_plural = _('Expenses')


class Revenue(models.Model):
    name = models.CharField(max_length=150, verbose_name=_('Name'))
    value = models.FloatField(verbose_name=_('Value'))
    approved = models.BooleanField(default=False, verbose_name=_('Approved'))
    created_at = models.DateTimeField(auto_now=True, verbose_name=_('Created at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Revenue')
        verbose_name_plural = _('Revenues')


class InsurancePrimary(models.Model):
    REFUND_CHOICES = (
        ('cash', 'cash'),
        ('bank', 'bank'),
    )

    name = models.CharField(max_length=100, verbose_name=_('Name'))
    value = models.FloatField(verbose_name=_('Value'))
    refunded = models.BooleanField(default=False, verbose_name=_('Refunded'))
    refunded_by = models.CharField(max_length=100, choices=REFUND_CHOICES, verbose_name=_('Refunded by'), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    class Meta:
        verbose_name = _('Insurance Primary')
        verbose_name_plural = _('Insurance Primary')


class InsuranceFinal(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    value = models.FloatField(verbose_name=_('Value'))
    refund_date = models.DateField(verbose_name=_('Refund date'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    class Meta:
        verbose_name = _('Insurance Final')
        verbose_name_plural = _('Insurance Final')