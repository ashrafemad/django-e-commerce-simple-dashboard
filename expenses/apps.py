from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ExpensesConfig(AppConfig):
    name = 'expenses'
    verbose_name = _('Expenses and Revenues')
