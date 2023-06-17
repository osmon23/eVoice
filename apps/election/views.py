from django.shortcuts import render, get_object_or_404
from .models import Election, ReferendumType
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ElectionSerializer, ReferendumTypeSerializer


class ElectionListView(APIView):
    def get(self, request):
        elections = Election.objects.all()
        serializer = ElectionSerializer(elections, many=True)
        return Response(serializer.data)


class ElectionDetailView(APIView):
    def get(self, request, election_id):
        election = get_object_or_404(Election, pk=election_id)
        serializer = ElectionSerializer(election)
        return Response(serializer.data)


class ReferendumListView(APIView):
    def get(self, request):
        referendum = ReferendumType.objects.all()
        serializer = ReferendumTypeSerializer(referendum)
        return Response(serializer.data)


class ReferendumTypeDetailView(APIView):
    def get(self, request, referendum_id):
        referendum = get_object_or_404(ReferendumType, pk=referendum_id)
        serializer = ReferendumTypeSerializer(referendum)
        return Response(serializer.data)
