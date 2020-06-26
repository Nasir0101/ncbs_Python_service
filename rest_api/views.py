from django.http import JsonResponse

from rest_api.serializers.PakistanCensusPercentageDataSerializer import PakistanCensusPercentageDataSerializer
from rest_api.serializers.PakistanDetailCensusDataSerializer import PakistanDetailCensusDataSerializer
from rest_api.serializers.PakistanPopulationByYearSerializer import PakistanPopulationByYearSerializer
from rest_api.serializers.PakistanProjectedPopulationByYearSerializer import PakistanProjectedPopulationByYearSerializer
from rest_api.serializers.WorldPopulationByCountryNameSerializer import WorldPopulationByCountryNameSerializer
from rest_api.serializers.WorldPopulationGrowthRateSerializer import WorldPopulationGrowthRateSerializer
from rest_api.serializers.WorldPopulationProjectedGrowthRateSerializer import \
    WorldPopulationProjectedGrowthRateSerializer
from rest_api.services.CensusRestService import CensusRestService


def getWorldPopulationData(request):
    queryset = CensusRestService.getWorldPopulationData()
    return JsonResponse(
        {'WorldPopulationByCountryName': WorldPopulationByCountryNameSerializer(queryset, many=True).data}, safe=False)


def getWorldPopulationGrowthRate(request):
    queryset = CensusRestService.getWorldPopulationGrowthRate()
    return JsonResponse({'WorldPopulationGrowthRate': WorldPopulationGrowthRateSerializer(queryset, many=True).data},
                        safe=False)


def getWorldPopulationProjectedGrowthRate(request):
    queryset = CensusRestService.getWorldPopulationProjectedGrowthRate()
    return JsonResponse(
        {'WorldPopulationProjectedGrowthRate': WorldPopulationProjectedGrowthRateSerializer(queryset, many=True).data},
        safe=False)


def getpakistanPopulationByYear(request):
    queryset = CensusRestService.getpakistanPopulationByYear()
    return JsonResponse({'PakistanPopulationByYear': PakistanPopulationByYearSerializer(queryset, many=True).data},
                        safe=False)


def getpakistanProjectedPopulationByYear(request):
    queryset = CensusRestService.getpakistanProjectedPopulationByYear()
    return JsonResponse(
        {'PakistanProjectedPopulationByYear': PakistanProjectedPopulationByYearSerializer(queryset, many=True).data},
        safe=False)


def getPakistanDetailCensusData(request, city):
    queryset = CensusRestService.getPakistanDetailCensusData(city)
    return JsonResponse({'PakistanDetailCensusData': PakistanDetailCensusDataSerializer(queryset, many=True).data},
                        safe=False)


def getPakistanPercentageCensusData(request, city):
    queryset = CensusRestService.getPakistanPercentageCensusData(city)
    return JsonResponse(
        {'PakistanCensusPercentageData': PakistanCensusPercentageDataSerializer(queryset, many=True).data}, safe=False)


def getProvince(request):
    province_list = CensusRestService.getProvince()
    return JsonResponse(province_list, safe=False)


def getCites(request, province):
    city_list = CensusRestService.getCites(province)
    return JsonResponse(city_list, safe=False)
