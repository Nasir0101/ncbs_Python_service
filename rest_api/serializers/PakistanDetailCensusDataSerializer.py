from rest_framework import serializers

from import_Data.models import PakistanDetailCensusData, PakistanCensusPercentageData


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


class PakistanDetailCensusDataSerializer(serializers.ModelSerializer):
    percentage_data = PakistanCensusPercentageDataSerializer(read_only=True)
    
    class Meta:
        model = PakistanDetailCensusData
        fields = (
            'id',
            'city',
            'province',
            'area',
            'population_1998',
            'male_pop',
            'female_pop',
            'sex_ratio',
            'population_density',
            'urban_population',
            'rural_population',
            'average_household_size',
            'literacy_ratio',
            'male_literacy_ratio',
            'female_literacy_ratio',
            'population_1981',
            'annual_growth_rate',
            'total_housing_unit',
            'pacca_housing_unit',
            'electricity_housing_unit',
            'water_housing_unit',
            'gas_housing_unit',
            'tehsils',
            'union_councils',
            'mauzas',
            'municipal_committees',
            'town_committees',
            'percentage_data')
