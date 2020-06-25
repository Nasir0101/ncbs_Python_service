import csv

from import_Data.models import PakistanDetailCensusData, PakistanCensusPercentageData


class ImportCensusDataService():
    
    @classmethod
    def importCensusData(cls):
        filename = "C:/Users/nasir/Downloads/FYP_CSV/Pakdetailcensusdata.csv"
        rows = []
        with open(filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)
            for row in csvreader:
                rows.append(row)
        for row in rows:
            PakistanDetailCensusData.objects.create(
                city=row[0],
                province=row[1],
                area=row[2],
                population_1998=row[3],
                male_pop=row[4],
                female_pop=row[5],
                sex_ratio=row[6],
                population_density=row[7],
                urban_population=row[8],
                rural_population=row[9],
                average_household_size=row[10],
                literacy_ratio=row[11],
                male_literacy_ratio=row[12],
                female_literacy_ratio=row[13],
                population_1981=row[14],
                annual_growth_rate=row[15],
                total_housing_unit=row[16],
                pacca_housing_unit=row[17],
                electricity_housing_unit=row[18],
                water_housing_unit=row[19],
                gas_housing_unit=row[20],
                tehsils=row[21],
                union_councils=row[22],
                mauzas=row[23],
                municipal_committees=row[24],
                town_committees=row[25])
            print("Data Saved", row)
        
        return "Detail Census Data imported Successfully"
    
    @classmethod
    def importCensusPercentageData(cls):
        filename = "C:/Users/nasir/Downloads/FYP_CSV/pakpercentagecensusdata.csv"
        rows = []
        with open(filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)
            for row in csvreader:
                rows.append(row)
        for row in rows:
            PakistanCensusPercentageData.objects.create(
                city=row[0],
                province=row[1],
                male_pop=row[2],
                female_pop=row[3],
                urban_pop=row[4],
                rural_pop=row[5],
                pacca_housing_unit=row[6],
                electricity_housing_unit=row[7],
                water_housing_unit=row[8],
                gas_housing_unit=row[9])
            print("Data Saved", row)
        
        return "Census Percentage Data imported Successfully"
