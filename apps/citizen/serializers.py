from rest_framework import serializers

from apps.citizen.models import Referendum, Citizen


class ReferendumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referendum
        fields = (
            'id',
            'INN',
            'biometry',
            'photo',
            'choice',
            'election',
        )


class CitizenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citizen
        fields = (
            'id',
            'phone_number',
            'email',
            'video',
            'candidate',
            'status',
        )
