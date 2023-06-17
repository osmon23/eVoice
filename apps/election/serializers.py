from datetime import date
from rest_framework import serializers
from .models import Election


def get_is_active(obj):
    return obj.end_date < date.today()


class ElectionSerializer(serializers.ModelSerializer):
    is_active = serializers.SerializerMethodField()

    class Meta:
        model = Election
        fields = '__all__'

