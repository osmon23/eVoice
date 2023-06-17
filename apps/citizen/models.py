from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail


from phonenumber_field.modelfields import PhoneNumberField

from .constants import StatusChoice, Choices
from apps.election.models import Candidate, Election


class Referendum(models.Model):
    INN = models.PositiveSmallIntegerField(
        _('INN'),
        unique=True,
    )
    biometry = models.CharField(
        _('Biometry'),
    )
    photo = models.ImageField(
        _('Photo'),
        upload_to='citizen/photo',
    )
    choice = models.CharField(
        _('Choice'),
        choices=Choices.CHOICES,
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
        verbose_name = _('Refere')
        verbose_name_plural = _('Refere')


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
        choices=StatusChoice.CHOICES,
    )

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _('Candidate')
        verbose_name_plural = _('Candidates')

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
