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
    photo = serializers.CharField(read_only=True)
    video = serializers.CharField(read_only=True)
    status = serializers.CharField(read_only=True)

    class Meta:
        model = Citizen
        fields = (
            'id',
            'INN',
            'biometry',
            'phone_number',
            'email',
            'photo',
            'video',
            'election',
            'candidate',
            'status',
        )
