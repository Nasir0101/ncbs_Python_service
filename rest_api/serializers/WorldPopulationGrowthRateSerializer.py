from rest_framework import serializers

from import_Data.models import WorldPopulationGrowthRate


class WorldPopulationGrowthRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorldPopulationGrowthRate
        fields = ('id', 'year', 'value', 'growthRate')
