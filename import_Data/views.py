from django.http import JsonResponse

from .importService import importService


def importWorldPopulationData(request):
    response = importService.importWorldPopulationData()
    return JsonResponse(response, status=200, safe=False)


def importWorldPopulationGrowthRate(request):
    response = importService.importWorldPopulationGrowthRate()
    return JsonResponse(response, status=200, safe=False)


def importWorldPopulationProjectedGrowthRate(request):
    response = importService.importWorldPopulationProjectedGrowthRate()
    return JsonResponse(response, status=200, safe=False)


def pakistanPopulationByYear(request):
    response = importService.pakistanPopulationByYear()
    return JsonResponse(response, status=200, safe=False)


def pakistanProjectedPopulationByYear(request):
    response = importService.pakistanProjectedPopulationByYear()
    return JsonResponse(response, status=200, safe=False)
