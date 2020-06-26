from rest_framework import serializers

from import_Data.models import WorldPopulationByCountryName


class WorldPopulationByCountryNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorldPopulationByCountryName
        fields = ('id', 'name', 'population', 'area', 'Density', 'WorldPercentage', 'rank')
