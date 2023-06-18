from django.shortcuts import render, get_object_or_404
from .models import Election
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ElectionSerializer


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
