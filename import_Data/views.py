from django.http import JsonResponse

from import_Data.services.ImportCensusDataService import ImportCensusDataService
from import_Data.services.importPopulationService import ImportPopulationService


def importWorldPopulationData(request):
    response = ImportPopulationService.importWorldPopulationData()
    return JsonResponse(response, status=200, safe=False)


def importWorldPopulationGrowthRate(request):
    response = ImportPopulationService.importWorldPopulationGrowthRate()
    return JsonResponse(response, status=200, safe=False)


def importWorldPopulationProjectedGrowthRate(request):
    response = ImportPopulationService.importWorldPopulationProjectedGrowthRate()
    return JsonResponse(response, status=200, safe=False)


def pakistanPopulationByYear(request):
    response = ImportPopulationService.pakistanPopulationByYear()
    return JsonResponse(response, status=200, safe=False)


def pakistanProjectedPopulationByYear(request):
    response = ImportPopulationService.pakistanProjectedPopulationByYear()
    return JsonResponse(response, status=200, safe=False)


def importPakistanDetailCensusData(request):
    response = ImportCensusDataService.importCensusData()
    return JsonResponse(response, status=200, safe=False)


def importPakistanPercentageCensusData(request):
    response = ImportCensusDataService.importCensusPercentageData()
    return JsonResponse(response, status=200, safe=False)