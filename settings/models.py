from django.db import models
from solo.models import SingletonModel
from django.utils.translation import gettext_lazy as _


class StartBalance(SingletonModel):
    bank = models.FloatField(verbose_name=_('Bank balance'), default=0)
    cash = models.FloatField(verbose_name=_('Cash balance'), default=0)

    class Meta:
        verbose_name = _('Start balance')
