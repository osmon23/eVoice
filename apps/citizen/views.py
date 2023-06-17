from rest_framework import viewsets

from .models import Referendum, Citizen
from .serializers import ReferendumSerializer, CitizenSerializer


class ReferendumViewSet(viewsets.ModelViewSet):
    queryset = Referendum.objects.all()
    serializer_class = ReferendumSerializer


class CitizenViewSet(viewsets.ModelViewSet):
    queryset = Citizen.objects.all()
    serializer_class = CitizenSerializer
