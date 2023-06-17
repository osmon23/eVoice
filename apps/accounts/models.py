from django.core.mail import send_mail
from django.db import models

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, UserManager

from phonenumber_field.modelfields import PhoneNumberField

#
# class CustomUserManager(UserManager):
#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)
#         return self._create_user(email, password, **extra_fields, create_superuser=True)


class Worker(AbstractUser):
    first_name = models.CharField(
        _('first name'),
        max_length=50,
    )
    last_name = models.CharField(
        _('last name'),
        max_length=50,
    )
    email = models.EmailField(
        _('email address'),
        unique=True,
    )
    phone_number = PhoneNumberField(
        _('phone number'),
        unique=True,
    )
    image = models.ImageField(
        _('image'),
        upload_to='users_images',
        null=True,
        blank=True,
    )
    inn = models.PositiveIntegerField(
        _('inn'),
        unique=True,
        null=True,
        blank=True,
    )
    position = models.CharField(
        _('position'),
        max_length=50,
    )

    objects = UserManager()

    class Meta:
        verbose_name = _("worker")
        verbose_name_plural = _("workers")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

