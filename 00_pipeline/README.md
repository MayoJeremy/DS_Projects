# Übungs-/Lernprojekt
# ETL Example Pipeline
ETL steht für Extract - Transform - Load

## Mkdocs
Mit mkdocs kann man u.a. auf Basis der Funktions- und Moduldocstrings
eine Dokumentation erstellen.

    pip install mkdocs
    pip install "mkdocstrings[python]"

## Mkdocs im Rootverzeichnis des Projekts initialisieren

    cd projects/pipeline
    mkdocs new .

## Mkdocs Dateien unter docs anlegen
z.B. reference .d

## Mkdocs Server starten

    mkdocs serve

## Mkdocs Build (statische HTML-Seite erzeugen)
HTML-Seiten werden erzeugt und unter /site abgelegt

    mkdocs build

## Python-Webserver starten
in /site

    python -m http.server