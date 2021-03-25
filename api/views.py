from rest_framework import viewsets

from .models import Table, Leg, Feet
from .serializers import TableSerializer, LegSerializer, FeetSerializer


class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all().order_by('name')
    serializer_class = TableSerializer


class LegViewSet(viewsets.ModelViewSet):
    queryset = Leg.objects.all().order_by('name')
    serializer_class = LegSerializer


class FeetViewSet(viewsets.ModelViewSet):
    queryset = Feet.objects.all().order_by('name')
    serializer_class = FeetSerializer

