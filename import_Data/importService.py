import csv

from .models import WorldPopulationByCountryName, WorldPopulationGrowthRate, WorldPopulationProjectedGrowthRate, \
    PakistanPopulationByYear, PakistanProjectedPopulationByYear


class importService():

    @classmethod
    def importWorldPopulationData(cls):
        filename = "C:/Users/nasir/Downloads/FYP_CSV/worldpopbycountryname.csv"
        rows = []
        with open(filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)
            for row in csvreader:
                rows.append(row)
        for row in rows:
            WorldPopulationByCountryName.objects.create(
                name=row[0],
                population=row[1],
                area=row[2],
                Density=row[3],
                WorldPercentage=row[4],
                rank=row[5])
            print("Data Saved", row)

        return "Data imported Successfully"

    @classmethod
    def importWorldPopulationGrowthRate(cls):
        filename = "C:/Users/nasir/Downloads/FYP_CSV/worldpopgrowthrate.csv"
        rows = []
        with open(filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)
            for row in csvreader:
                rows.append(row)
        for row in rows:
            WorldPopulationGrowthRate.objects.create(
                year=row[0],
                value=row[1],
                growthRate=row[2])
            print("Data Saved", row)

        return "Data imported Successfully"

    @classmethod
    def importWorldPopulationProjectedGrowthRate(cls):
        filename = "C:/Users/nasir/Downloads/FYP_CSV/worldpopprojectedgrowth.csv"
        rows = []
        with open(filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)
            for row in csvreader:
                rows.append(row)
        for row in rows:
            WorldPopulationProjectedGrowthRate.objects.create(
                year=row[0],
                value=row[1],
                growthRate=row[2])
            print("Data Saved", row)

        return "Data imported Successfully"

    @classmethod
    def pakistanPopulationByYear(cls):
        filename = "C:/Users/nasir/Downloads/FYP_CSV/pakpopbyyear.csv"
        rows = []
        with open(filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)
            for row in csvreader:
                rows.append(row)
        for row in rows:
            PakistanPopulationByYear.objects.create(
                year=row[0],
                totalPopulation=row[1],
                growthRate=row[2],
                density=row[3],
                totalPopulationRank=row[4],
                densityRank=row[5]
            )
            print("Data Saved", row)

        return "Data imported Successfully"

    @classmethod
    def pakistanProjectedPopulationByYear(cls):
        filename = "C:/Users/nasir/Downloads/FYP_CSV/pakprojectedpopbyyear.csv"
        rows = []
        with open(filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)
            for row in csvreader:
                rows.append(row)
        for row in rows:
            PakistanProjectedPopulationByYear.objects.create(
                year=row[0],
                totalPopulation=row[1],
                growthRate=row[2],
                density=row[3],
                PopulationRank=row[4],
                densityRank=row[5]
            )
            print("Data Saved", row)

        return "Data imported Successfully"
