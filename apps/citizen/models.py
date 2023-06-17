from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail


from phonenumber_field.modelfields import PhoneNumberField

from .constants import StatusChoice, Choices
from apps.election.models import Election
from apps.candidates.models import Candidate


class Referendum(models.Model):
    INN = models.PositiveSmallIntegerField(
        _('INN'),
        unique=True,
    )
    biometry = models.CharField(
        _('Biometry'),
        max_length=100,
    )
    photo = models.ImageField(
        _('Photo'),
        upload_to='citizen/photo',
    )
    choice = models.CharField(
        _('Choice'),
        choices=Choices.choices,
        max_length=100,
    )
    election = models.ForeignKey(
        Election,
        on_delete=models.CASCADE,
        verbose_name=_('Election'),
        related_name='elections',
    )
    email = models.EmailField(
        _('Email Address'),
        unique=True,
    )

    def __str__(self):
        return self.INN

    class Meta:
        verbose_name = _('Referendum')
        verbose_name_plural = _('Referendums')


class Citizen(Referendum, models.Model):
    phone_number = PhoneNumberField(
        _('Phone Number'),
        unique=True,
    )
    video = models.FileField(
        _('Video'),
        upload_to='citizen/video',
    )
    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
        verbose_name=_('Candidate'),
        related_name='candidates',
    )
    status = models.CharField(
        _('Status'),
        choices=StatusChoice.choices,
        max_length=100,
    )

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _('Citizen')
        verbose_name_plural = _('Citizens')

    def save(self, *args, **kwargs):
        if self.status == StatusChoice.APPROVED:
            send_mail(
                'Elections',
                'Hello, your vote has been counted',
                'dastiw1910@gmail.com',
                [self.email],
                fail_silently=False,
            )
        elif self.status == StatusChoice.REFUSED:
            send_mail(
                'Elections',
                'Hello, your vote has been rejected, please try again',
                'dastiw1910@gmail.com',
                [self.email],
                fail_silently=False,
            )
        return super().save(*args, **kwargs)
