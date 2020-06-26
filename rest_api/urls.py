from django.urls import path

from . import views

urlpatterns = [
    path('world/population/data', views.getWorldPopulationData),
    path('world/population/growthrate', views.getWorldPopulationGrowthRate),
    path('world/population/projected/growthrate', views.getWorldPopulationProjectedGrowthRate),
    path('pakistan/population/by/year', views.getpakistanPopulationByYear),
    path('pakistan/projected/population/by/year', views.getpakistanProjectedPopulationByYear),
    path('pakistan/detail/censusdata/<str:city>', views.getPakistanDetailCensusData),
    path('pakistan/percentage/censusdata/<str:city>', views.getPakistanPercentageCensusData),
    path('province', views.getProvince),
    path('cities/<str:province>', views.getCites)
]
