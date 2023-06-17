from django.db import models
from django.utils.translation import gettext_lazy as _


class Choices(models.IntegerChoices):
    ACCEPT = 'A', _('Accept')
    REJECT = 'R', _('Reject')


class StatusChoice(models.TextChoices):
    VERIFY = 'V', _('Verify')
    APPROVED = 'A', _('Approved')
    REFUSED = 'R', _('Refused')
