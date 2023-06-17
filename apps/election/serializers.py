from datetime import date
from rest_framework import serializers
from .models import Election, ReferendumType


class ElectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Election
        fields = '__all__'


class ReferendumTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferendumType
        fields = '__all__'
