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
