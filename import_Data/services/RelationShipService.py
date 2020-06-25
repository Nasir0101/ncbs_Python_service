from import_Data.models import PakistanDetailCensusData, PakistanCensusPercentageData


class RelationShipService:
    
    @classmethod
    def DetailCensusDataToPercentageDataRelationShip(cls):
        detailCensusData = PakistanDetailCensusData.objects.all()
        for row in detailCensusData:
            percentageDataId = PakistanCensusPercentageData.objects.filter(city=row.city).first()
            row.percentage_data_id = percentageDataId.id
            row.save()
            print("Add ", percentageDataId.id, " for city ", row.city)
        return 'Relation Added Successfully'
