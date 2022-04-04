# WFS_Downloader
The WFS_Downloader is a small tool with a Graphical User Interface to easily use [the "ogc_api" of the state North-Rhine-Westphalia in Germany](https://ogc-api.nrw.de/lika/v1 "API documentation (mostly in german)")

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [License](#license)


## General Information
The program has been devoleped to use the API easily and also productive with a lot of data at once.
At the time of writing, it is only possible to ask only for one object at once.
With the WFS_Downloader at the current stage it is possible to dowmload the data for a whole excel list at once.
Furthermore the program transforms the `.json` file returned by the API in a `.gpkg` file with all requested objects in one file.


## Technologies Used
- Fiona - version 1.8.21
- GDAL - version 3.4.2
- see [requirements.txt](bin/requirements.txt)


## Features
- Most of the changeable settings (e.g. program name or colors) can be configured in the `settings.json` file
- Converts the returned objects by the API from multipolygons to polygons


## Setup
### With release file
1. Download the latest release file for your computer
2. Start the program

### From Source Code
1. Download the code
2. Install the [requirements.txt](bin/requirements.txt) with `pip`
3. Install [GDAL](https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal "External site with wheel files for a lot of important packages") with the wheel file matching your computer
4. Install [Fiona](https://www.lfd.uci.edu/~gohlke/pythonlibs/#fiona "External site with wheel files for a lot of important packages") with the wheel file matching your computer
5. Run the [main.py](main.py) file


## Usage
### Input
The excel file has to have the right layout to be compatible with the program.
Important are the name of the columns wich are containing the parameters to build the object Id for the API ("Flurstückskennzeichen").
In the [example.xlsx](bin/examples.xlsx), the first five columns are prequisite, the last two are optional.

### Output
The output (`.gpkg`) is optimised for using with [QGIS](https://qgis.org/en/site/ "QGIS Homepage") and uses the coordinate system EPSG:25832.
The data downloaded alongside wth the coordinates can also be easily viewed in QGIS


## Project Status
Project is: _in progress_


## License
This project is open source and available under the [GNUv3.0 License](LICENSE.md).
