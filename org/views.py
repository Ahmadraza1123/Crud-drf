from rest_framework import viewsets
from .models import Company, Branch, Building, Floor, Room
from .serializers import (
    CompanySerializer, BranchSerializer, BuildingSerializer, FloorSerializer, RoomSerializer
)

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all().prefetch_related(
        'branches__buildings__floors__rooms'
    )
    serializer_class = CompanySerializer

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.select_related('company').prefetch_related(
        'buildings__floors__rooms'
    )
    serializer_class = BranchSerializer

class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.select_related('branch__company').prefetch_related(
        'floors__rooms'
    )
    serializer_class = BuildingSerializer

class FloorViewSet(viewsets.ModelViewSet):
    queryset = Floor.objects.select_related('building__branch__company').prefetch_related(
        'rooms'
    )
    serializer_class = FloorSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.select_related('floor__building__branch__company')
    serializer_class = RoomSerializer

