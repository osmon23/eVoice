from django.db import models
from django.utils.translation import gettext_lazy as _


class Choices(models.IntegerChoices):
    ACCEPT = True, _('Accept')
    REJECT = False, _('Reject')


class StatusChoice(models.TextChoices):
    VERIFY = 'V', _('Verify')
    APPROVED = 'A', _('Approved')
    REFUSED = 'R', _('Refused')
