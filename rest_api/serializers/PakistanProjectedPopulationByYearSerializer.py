from rest_framework import serializers

from import_Data.models import PakistanProjectedPopulationByYear


class PakistanProjectedPopulationByYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = PakistanProjectedPopulationByYear
        fields = ('id', 'year', 'totalPopulation', 'growthRate', 'density', 'PopulationRank', 'densityRank')
