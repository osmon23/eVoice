from rest_framework import serializers
from apps.candidates.models import Candidate


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'


class CandidateStatisticSerializer(serializers.ModelSerializer):
    counting = serializers.IntegerField(default=0)
    percentage = serializers.FloatField(default=0)

    class Meta:
        model = Candidate
        fields = ['party', 'counting', 'percentage']
