from rest_framework import serializers

from import_Data.models import PakistanCensusPercentageData


class PakistanCensusPercentageDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PakistanCensusPercentageData
        fields = (
            'id',
            'city',
            'province',
            'male_pop',
            'female_pop',
            'urban_pop',
            'rural_pop',
            'pacca_housing_unit',
            'electricity_housing_unit',
            'water_housing_unit',
            'gas_housing_unit')
