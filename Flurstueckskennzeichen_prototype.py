import geopandas as gpd
import pandas as pd
import requests
import json
import os


class Flurstueckskennzeichen:
    def __init__(self, source_path, target_path):
        self.Land = str
        self.Gemarkungsnummer = str
        self.Flurnummer = str
        self.Zaehler = str
        self.Nenner = str
        self.Flurstuecksfolge = str

        # Reads the Excel file
        self.raw_data = pd.read_excel(rf"{source_path}", dtype='str')
        rows = len(self.raw_data)

        i = 0
        while i != rows:
            flurstueckskennzeichen = self.form_kennzeichen(i)
            self.get_from_api(flurstueckskennzeichen)

            i = i + 1

        self.gjson_to_gpkg(target_path)

    @staticmethod
    def get_from_api(flurstueckskennzeichen):
        # URL to the ogc-api and inserts the identifier
        url = f"https://ogc-api.nrw.de/lika/v1/collections/flurstueck/items/{flurstueckskennzeichen}?crs=http%3A%2F" \
              f"%2Fwww.opengis.net%2Fdef%2Fcrs%2FEPSG%2F0%2F25832&f=json&skipGeometry=false"

        # Requests the JSON file from the API and loads it as JSON
        output = requests.get(url).json()

        # Saves the JSON file
        with open(f'bin/inputs/{flurstueckskennzeichen}.json', 'a+') as file:
            json.dump(output, file)

        # Further API documentation
        # https://ogc-api.nrw.de/lika/v1

    def form_kennzeichen(self, row):

        # Connects the parts of the flurstueckskennzeichen
        self.Land = self.raw_data.iloc[row]["Land"]
        self.Gemarkungsnummer = self.raw_data.iloc[row]["Gemarkungsnummer"]
        self.Flurnummer = self.raw_data.iloc[row]["Flurnummer"]
        self.Zaehler = self.raw_data.iloc[row]["Zähler"]
        self.Nenner = self.raw_data.iloc[row]["Nenner"]
        self.Flurstuecksfolge = self.raw_data.iloc[row]["Flurstücksfolge"]

        composed = self.Land + self.Gemarkungsnummer + self.Flurnummer + self.Zaehler + self.Nenner + self.Flurstuecksfolge

        # Checks for an Error (the flurstueckskennzeichen is always 20 characters long)
        if len(composed) == 20:
            return composed

        # Structure of the flurstueckskennzeichen
        # https://www.adv-online.de/AdV-Produkte/Liegenschaftskataster/ALKIS/binarywriterservlet?imgUid=8c860f61-34ab-4a41-52cf-b581072e13d6&uBasVariant=11111111-1111-1111-1111-111111111111#_C11520-_A11520_49472

    @staticmethod
    def gjson_to_gpkg(target_location):
        # Gets all filenames in the directory
        file = os.listdir(rf"C:\Users\Konrad\Documents\IT\python\ogr_test\bin\inputs")
        # Adds all .json files to path
        path = [os.path.join(rf"C:\Users\Konrad\Documents\IT\python\ogr_test\bin\inputs", i) for i in file if
                ".json" in i]

        # Merges all files in path to GeoDataFrame raw_data
        raw_data = gpd.GeoDataFrame(pd.concat([gpd.read_file(i) for i in path]))

        # Resets Index because the Index has to be sorted for .explode
        raw_data = raw_data.reset_index(drop=True)
        # Converts Multipolygons to Polygons
        raw_data = raw_data.explode(index_parts=False)
        # Sets Coordinate System to EPSG:25832, ignores any problem (possible because the EPSG of the input is also
        # 25832)
        raw_data = raw_data.set_crs(25832, allow_override=True)

        # Saves raw_data as GeoPackage file
        raw_data.to_file(filename=rf"{target_location}\output.gpkg", driver="GPKG")

        # Further desription of some code parts
        # https://stackoverflow.com/questions/48874113/concat-multiple-shapefiles-via-geopandas
        # https://github.com/geopandas/geopandas/issues/1223

        # Needs to be downloaded and installed via pip
        # https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal
        # https://www.lfd.uci.edu/~gohlke/pythonlibs/#fiona


Flurstueckskennzeichen("C:/Users/Konrad/Desktop/GIS_API.xlsx", "C:/Users/Konrad/Desktop")
