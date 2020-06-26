from rest_framework import serializers

from import_Data.models import WorldPopulationProjectedGrowthRate


class WorldPopulationProjectedGrowthRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorldPopulationProjectedGrowthRate
        fields = ('id', 'year', 'value', 'growthRate')
