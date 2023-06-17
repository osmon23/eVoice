from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.election.models import Election


class Candidate(models.Model):
    election = models.ForeignKey(
        Election,
        on_delete=models.CASCADE,
        related_name='election_candidates',
        verbose_name=_('Election')
        )
    name = models.CharField(
        _('name'), 
        max_length=100
        )
    age = models.PositiveIntegerField(
        _('age')
    )
    party = models.CharField(
        _('party'), 
        max_length=100
        )
    experience = models.CharField(
        _('experience'), 
        max_length=255
        )
    biography = models.TextField(
        _('biography'),
        max_length=500,
    )
    photo = models.ImageField(
        _('photo'), 
        upload_to='candidate_photos/'
        )

    class Meta:
        verbose_name = _('Candidate')
        verbose_name_plural = _('Candidates')

    def __str__(self):
        return self.name



