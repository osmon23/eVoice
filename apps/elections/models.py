from django.db import models
from django.utils.translation import ugettext_lazy as _


class ElectionType(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=100
        )

    def __str__(self):
        return self.name


class Election(models.Model):
    title = models.CharField(
        _('Title'),
        max_length=100
        )
    description = models.TextField(_('Description'))
    start_date = models.DateTimeField(_('Start_date'))
    end_date = models.DateTimeField(_('End_date'))
    election_type = models.ForeignKey(
        _('Election_type'), 
        ElectionType, 
        on_delete=models.CASCADE
        )

    def __str__(self):
        return self.title


class Candidate(models.Model):
    election = models.ForeignKey(
        _('Election'), 
        Election, 
        on_delete=models.CASCADE
        )
    name = models.CharField(
        _('Name'), 
        max_length=100
        )
    age = models.IntegerField(_('Age'))
    party = models.CharField(
        _('Party'), 
        max_length=100
        )
    experience = models.CharField(
        _('Experience'), 
        max_length=255
        )
    biography = models.TextField(_('Biography'))
    photo = models.ImageField(
        _('Photo'), 
        upload_to='candidate_photos/'
        )

    def __str__(self):
        return self.name
