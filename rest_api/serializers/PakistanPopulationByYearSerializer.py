from rest_framework import serializers

from import_Data.models import PakistanPopulationByYear


class PakistanPopulationByYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = PakistanPopulationByYear
        fields = ('id', 'year', 'totalPopulation', 'growthRate', 'density', 'totalPopulationRank', 'densityRank')
