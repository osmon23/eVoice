from django.db import models
from django.utils.translation import gettext_lazy as _


class StatusChoice(models.TextChoices):
    VERIFY = 'V', _('Verify')
    APPROVED = 'A', _('Approved')
    REFUSED = 'R', _('Refused')


class Choices(models.IntegerChoices):
    ACCEPT = 'A', _('Accept')
    REJECT = 'R', _('Reject')
