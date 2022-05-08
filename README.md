# WFS_Downloader
Der WFS_Downloader ist ein kleines Programm mit Grafischer Nutzeroberfläche um die ["ogc_api" von Nordrhein-Westfalen](https://ogc-api.nrw.de/lika/v1 "Dokumentation der API") einfach verwenden zu können.

## Inhaltsverzeichnis
* [Allgemeines](#Allgemeines)
* [Verwendete Packages](#Verwendete-Packages)
* [Features](#Features)
* [Installation](#Installation)
* [Verwendung](#Verwendung)
* [Projektstatus](#Projektstatus)
* [Lizenz](#Lizenz)


## Allgemeines
Das Programm wurde entwickelt, um die API schnell und einfach mit einer Menge an Daten verwenden zu können.
Mit der aktuellen Version des WFS_Downloaders ist es möglich die Flurstückkennzeichen aus einer Tabelle heraus zu bilden, diese bei der API abzufragen und herunterzuladen.
Weiterhin konvertiert das Programm die ".json"-Datei, die von der API für jedes abgefragte Objekt ausgegeben wird, in eine ".gpkg"-Datei für alle abgefragten Objekte.


## Verwendete Packages
- Fiona - Version 1.8.21
- GDAL - Version 3.4.2
- Siehe auch: [requirements.txt](bin/requirements.txt)


## Features
- Ein Großteil der Einstellungen (z.B. der Name des Programms oder die Farben) lassen sich über die "settings.json"-Datei einfach ändern
- Konvertiert die Ausgabe der API von Multipolygonen zu Polygonen


## Installation
### Mit Release File --- Noch nicht möglich
1. Laden Sie das aktuellste Release File herunter
2. Starten Sie das Programm

### Vom Quellcode
1. Laden Sie den Quellcode herunter
2. Installieren Sie die verwendeten Packages ([requirements.txt](bin/requirements.txt)) mit "pip"
3. Installieren Sie [GDAL](https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal "Externe Internetseite mit Wheel-Dateien für viele wichtige Packages") mit der zu Ihrem Computer passendem Wheel-Datei
4. Installieren Sie [Fiona](https://www.lfd.uci.edu/~gohlke/pythonlibs/#fiona "Externe Internetseite mit Wheel-Dateien für viele wichtige Packages") mit der zu Ihrem Computer passendem Wheel-Datei
5. Führen Sie die [main.py](main.py) Datei aus


## Verwendung
### Eingabe
Die Quelltabelle muss im ".xlsx" Format oder im ".xls" Format sein.
Wichtig sind die Titel der Spalten, die die Parameter des Flurstückskennzeichen beinhalten.
In der [example.xlsx](bin/example.xlsx) Datei sind die sieben Parameter als Spaltentitel zu sehen.
Die ersten fünf sind notwendig, die letzteren Beiden sind optional.

### Ausgabe
Die Ausgabe des Programms ist für die Nutzung mit [QGIS](https://qgis.org/en/site/ "QGIS Webseite") optimiert und nutzt das vom Land NRW standardmäßig verwendete Koordinatensystem EPSG:25832.
Die Daten zu den abgefragten Objekten können ebenfalls in QGIS angesehen werden.


## Projektstatus
Projektstatus ist: _in Arbeit_

Project is: _in progress_


## Lizenz
Dieses Projekt ist Open Source und verfügbar unter der [GPLv3.0 Lizenz](LICENSE.md).

This project is open source and available under the [GPLv3.0 License](LICENSE.md).
