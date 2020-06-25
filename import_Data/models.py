import uuid

from django.db import models


class WorldPopulationByCountryName(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(db_column='name', max_length=255, default="")
    population = models.CharField(db_column='population', max_length=255, default="")
    area = models.CharField(db_column='area', max_length=255, default="")
    Density = models.CharField(db_column="Density", max_length=255, default="")
    WorldPercentage = models.CharField(db_column="WorldPercentage", max_length=255, default="")
    rank = models.CharField(db_column="rank", max_length=255, default="")
    
    class Meta:
        db_table = 'world_pop_by_country_name'


class WorldPopulationGrowthRate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    year = models.CharField(db_column='year', max_length=255, default="")
    value = models.CharField(db_column='value', max_length=255, default="")
    growthRate = models.CharField(db_column="GrowthRate", max_length=255, default="")
    
    class Meta:
        db_table = 'world_pop_growth_rate'


class WorldPopulationProjectedGrowthRate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    year = models.CharField(db_column='year', max_length=255, default="")
    value = models.CharField(db_column='value', max_length=255, default="")
    growthRate = models.CharField(db_column="GrowthRate", max_length=255, default="")
    
    class Meta:
        db_table = 'world_pop_projected_growth_rate'


class PakistanPopulationByYear(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    year = models.CharField(db_column='year', max_length=255, default="")
    totalPopulation = models.CharField(db_column='totalPopulation', max_length=255, default="")
    growthRate = models.CharField(db_column='growthRate', max_length=255, default="")
    density = models.CharField(db_column="density", max_length=255, default="")
    totalPopulationRank = models.CharField(db_column="totalPopulationRank", max_length=255, default="")
    densityRank = models.CharField(db_column="densityRank", max_length=255, default="")
    
    class Meta:
        db_table = 'pakistan_population_by_year'


class PakistanProjectedPopulationByYear(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    year = models.CharField(db_column='year', max_length=255, default="")
    totalPopulation = models.CharField(db_column='totalPopulation', max_length=255, default="")
    growthRate = models.CharField(db_column='growthRate', max_length=255, default="")
    density = models.CharField(db_column="density", max_length=255, default="")
    PopulationRank = models.CharField(db_column="populationRank", max_length=255, default="")
    densityRank = models.CharField(db_column="densityRank", max_length=255, default="")
    
    class Meta:
        db_table = 'pakistan_projected_pop_by_year'


class PakistanCensusPercentageData(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    city = models.CharField(db_column='city', max_length=255, default="")
    province = models.CharField(db_column='province', max_length=255, default="")
    male_pop = models.FloatField(db_column='male_pop', default=0)
    female_pop = models.FloatField(db_column='female_pop', default=0)
    urban_pop = models.FloatField(db_column='urban_pop', default=0)
    rural_pop = models.FloatField(db_column='rural_pop', default=0)
    pacca_housing_unit = models.FloatField(db_column='pacca_housing_unit', default=0)
    electricity_housing_unit = models.FloatField(db_column='electricity_housing_unit', default=0)
    water_housing_unit = models.FloatField(db_column='water_housing_unit', default=0)
    gas_housing_unit = models.FloatField(db_column='gas_housing_unit', default=0)

    class Meta:
        db_table = 'pakistan_census_percentage_data'


class PakistanDetailCensusData(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    city = models.CharField(db_column='city', max_length=255, default="")
    province = models.CharField(db_column='province', max_length=255, default="")
    area = models.FloatField(db_column='area', default=0)
    population_1998 = models.FloatField(db_column='population_1998', default=0)
    male_pop = models.FloatField(db_column='male_pop', default=0)
    female_pop = models.FloatField(db_column='female_pop', default=0)
    sex_ratio = models.FloatField(db_column='sex_ratio', default=0)
    population_density = models.FloatField(db_column='population_density', default=0)
    urban_population = models.FloatField(db_column='urban_population', default=0)
    rural_population = models.FloatField(db_column='rural_population', default=0)
    average_household_size = models.FloatField(db_column='average_household_size', default=0)
    literacy_ratio = models.FloatField(db_column='literacy_ratio', default=0)
    male_literacy_ratio = models.FloatField(db_column='male_literacy_ratio', default=0)
    female_literacy_ratio = models.FloatField(db_column='female_literacy_ratio', default=0)
    population_1981 = models.FloatField(db_column='population_1981', default=0)
    annual_growth_rate = models.FloatField(db_column='annual_growth_rate', default=0)
    total_housing_unit = models.FloatField(db_column='total_housing_unit', default=0)
    pacca_housing_unit = models.FloatField(db_column='pacca_housing_unit', default=0)
    electricity_housing_unit = models.FloatField(db_column='electricity_housing_unit', default=0)
    water_housing_unit = models.FloatField(db_column='water_housing_unit', default=0)
    gas_housing_unit = models.FloatField(db_column='gas_housing_unit', default=0)
    tehsils = models.FloatField(db_column='tehsils', default=0)
    union_councils = models.FloatField(db_column='union_councils', default=0)
    mauzas = models.FloatField(db_column='mauzas', default=0)
    municipal_committees = models.FloatField(db_column='municipal_committees', default=0)
    town_committees = models.FloatField(db_column='town_committees', default=0)
    percentage_data = models.OneToOneField(PakistanCensusPercentageData, on_delete=models.CASCADE, null=True,
                                           unique=False)
    
    class Meta:
        db_table = 'pakistan_detail_census_data'
