from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name=_('Name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name=_('Name'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('Category'))
    mark = models.CharField(max_length=100, verbose_name=_('Mark'))
    model = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('Model'))
    part_number = models.CharField(max_length=100, default='-', verbose_name=_('Part number'))
    cost_price = models.FloatField(verbose_name=_('Cost price'))
    quantity = models.IntegerField(verbose_name=_('Quantity'))
    attributes = models.ManyToManyField('AttributeValue')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class Attribute(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Attribute')
        verbose_name_plural = _('Attributes')


class AttributeValue(models.Model):
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, verbose_name=_('Attribute'))
    value = models.CharField(max_length=100, verbose_name=_('Value'))

    def __str__(self):
        return f'{self.attribute.name}: {self.value}'

    class Meta:
        verbose_name = _('Attribute value')
        verbose_name_plural = _('Attribute values')
