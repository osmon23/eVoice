from datetime import timezone

from django.db import models
from django.utils.translation import gettext_lazy as _


class ElectionType(models.Model):
    id = models.AutoField(
        _('ID'),
        primary_key=True,
    )
    name = models.CharField(
        _('Name'),
        max_length=100,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("ElectionType")
        verbose_name_plural = _("ElectionTypes")


class Election(models.Model):
    title = models.CharField(
        _('Title'),
        max_length=100,
    )
    image = models.ImageField(
        _('Image'),
    )
    description = models.TextField(
        _('Description'),
        max_length=500,
    )
    start_date = models.DateField(
        _('Start_Date'),
    )
    end_date = models.DateField(
        _('End Date'),
    )
    election_type = models.ForeignKey(
        ElectionType,
        on_delete=models.CASCADE,
        verbose_name=_('Election Type'),
        related_name='Election',
    )
    is_active = models.BooleanField(
        _('is_active'),
        default=False,
    )

    def save(self, *args, **kwargs):
        if self.end_date < timezone.now().date():
            self.is_active = True
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Election")
        verbose_name_plural = _("Elections")