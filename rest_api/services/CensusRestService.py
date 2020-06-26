from import_Data.models import WorldPopulationByCountryName, WorldPopulationGrowthRate, \
    WorldPopulationProjectedGrowthRate, PakistanPopulationByYear, PakistanProjectedPopulationByYear, \
    PakistanDetailCensusData, PakistanCensusPercentageData


class CensusRestService:
    @classmethod
    def getWorldPopulationData(cls):
        queryset = WorldPopulationByCountryName.objects.all()
        return queryset
    
    @classmethod
    def getWorldPopulationGrowthRate(cls):
        queryset = WorldPopulationGrowthRate.objects.all()
        return queryset
    
    @classmethod
    def getWorldPopulationProjectedGrowthRate(cls):
        queryset = WorldPopulationProjectedGrowthRate.objects.all()
        return queryset
    
    @classmethod
    def getpakistanPopulationByYear(cls):
        queryset = PakistanPopulationByYear.objects.all()
        return queryset
    
    @classmethod
    def getpakistanProjectedPopulationByYear(cls):
        queryset = PakistanProjectedPopulationByYear.objects.all()
        return queryset
    
    @classmethod
    def getPakistanDetailCensusData(cls, city):
        queryset = PakistanDetailCensusData.objects.filter(city=city)
        return queryset
    
    @classmethod
    def getPakistanPercentageCensusData(cls, city):
        queryset = PakistanCensusPercentageData.objects.filter(city=city)
        return queryset
    
    @classmethod
    def getProvince(cls):
        province_list = list(PakistanCensusPercentageData.objects.values('province').distinct())
        return province_list
    
    @classmethod
    def getCites(cls, province):
        city_list = list(PakistanCensusPercentageData.objects.filter(province=province).values('city').distinct())
        return city_list
