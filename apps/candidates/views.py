from apps.candidates.models import Candidate
from apps.candidates.serializers import CandidateSerializer, CandidateStatisticSerializer
from rest_framework import viewsets
from django.db.models import Count


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class CandidateStatisticView(viewsets.ModelViewSet):
    serializer_class = CandidateStatisticSerializer
    queryset = Candidate.objects.all()
    lookup_field = 'election_pk'

    def get_queryset(self):
        election = self.kwargs['election_pk']
        filtering_by_election = Candidate.objects.filter(election=election)
        candidate_statistic = filtering_by_election.values('name').annotate(
            counting=Count('name'),
            percentage=Count('name')*100/len(filtering_by_election)
        )
        return candidate_statistic

