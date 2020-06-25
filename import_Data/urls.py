from django.urls import path

from . import views

urlpatterns = [
    path('world/population/data', views.importWorldPopulationData),
    path('world/population/growthrate', views.importWorldPopulationGrowthRate),
    path('world/population/projected/growthrate', views.importWorldPopulationProjectedGrowthRate),
    path('pakistan/population/by/year', views.pakistanPopulationByYear),
    path('pakistan/projected/population/by/year', views.pakistanProjectedPopulationByYear),
    path('pakistan/detail/censusdata', views.importPakistanDetailCensusData),
    path('pakistan/percentage/censusdata', views.importPakistanPercentageCensusData)
]
