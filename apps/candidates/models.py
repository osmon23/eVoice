from django.db import models
from django.utils.translation import ugettext_lazy as _
from apps.election.models import Election


class Candidate(models.Model):
    id = models.AutoField(
        _('id'),
        primary_key=True
        )
    election = models.ForeignKey(
        _('election'),
        Election,
        on_delete=models.CASCADE
        )
    name = models.CharField(
        _('name'), 
        max_length=100
        )
    age = models.IntegerField(_('age'))
    party = models.CharField(
        _('party'), 
        max_length=100
        )
    experience = models.CharField(
        _('experience'), 
        max_length=255
        )
    biography = models.TextField(_('biography'))
    photo = models.ImageField(
        _('photo'), 
        upload_to='candidate_photos/'
        )

    def __str__(self):
        return self.name
    

