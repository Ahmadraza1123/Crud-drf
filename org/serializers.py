from rest_framework import serializers
from .models import Company, Branch, Building, Floor, Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name', 'floor']

class FloorSerializer(serializers.ModelSerializer):
    rooms = RoomSerializer(many=True, read_only=True)
    class Meta:
        model = Floor
        fields = ['id', 'number', 'building', 'rooms']

class BuildingSerializer(serializers.ModelSerializer):
    floors = FloorSerializer(many=True, read_only=True)
    class Meta:
        model = Building
        fields = ['id', 'name', 'branch', 'floors']

class BranchSerializer(serializers.ModelSerializer):
    buildings = BuildingSerializer(many=True, read_only=True)
    class Meta:
        model = Branch
        fields = ['id', 'name', 'company', 'buildings']

class CompanySerializer(serializers.ModelSerializer):
    branches = BranchSerializer(many=True, read_only=True)
    class Meta:
        model = Company
        fields = ['id', 'name', 'branches']
