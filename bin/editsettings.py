import json

settings = {
    "main":
        [
            {
                "item": "program_name",
                "program_name": "WFS Downloader"
            },
            {
                "item": "window_title",
                "window_title": "Beta"
            },
            {
                "item": "geometry",
                "geometry": "900x600+120+120"
            },
            {
                "item": "icon",
                "icon": "bin/python_logo.png"
            }
        ],
    "color":
        [
            {
                "item": "standard",
                "background": "#97c11f"
            },
            {
                "item": "button",
                "background": "#afd4f1",
                "activebackground": "#afd4f1"
            },
            {
                "item": "back_button",
                "background": "#da5454",
                "activebackground": "white"
            },
            {
                "item": "entry",
                "background": "white",
                "selectbackground": "#0078D7",
                "selectforeground": "white"
            }
        ],
    "font":
        [
            {
                "item": "big",
                "font": "Bahnschrift 30"
            },
            {
                "item": "normal",
                "font": "Bahnschrift 15"
            },
            {
                "item": "normal_underlined",
                "font": "Bahnschrift 15 underline"
            },
            {
                "item": "small",
                "font": "Bahnschrift"
            }
        ],
    "text":
        [
            {
                "item": "variant_1",
                "text": "Flurstückabfrage mit Tabelle"
            },
            {
                "item": "variant_2",
                "text": "Variante 2"
            },
            {
                "item": "variant_3",
                "text": "Variante 3"
            },
            {
                "item": "variant_4",
                "text": "Variante 4"
            },
            {
                "item": "back_button",
                "text": "Zurück"
            },
            {
                "item": "start_button",
                "text": "Start"
            },
            {
                "item": "explorer_button",
                "text": "Auswählen"
            },
            {
                "item": "source_title_label",
                "text": "Quelle"
            },
            {
                "item": "source_entry_label",
                "text": "Dateipfad:"
            },
            {
                "item": "target_title_label",
                "text": "Ziel"
            },
            {
                "item": "target_entry_label",
                "text": "Ordnerpfad:"
            }
        ],
    "size":
        [
            {
                "item": "window_size",
                "width": 600,
                "height": 400
            },
            {
                "item": "relief",
                "borderwidth": 2
            }
        ],
    "relief":
        [
            {
                "item": "file_frame",
                "relief": "groove"
            }
        ],
    "error":
        [
            {
                "item": "error_101",
                "title": "Eingabefehler",
                "text": "Quellpfad ist falsch"
            },
            {
                "item": "error_102",
                "title": "Eingabefehler",
                "text": "Zielpfad ist falsch"
            },
            {
                "item": "error_103",
                "title": "Eingabefehler",
                "text": "Quell- und Zielpfad sind falsch"
            },
            {
                "item": "error_111",
                "title": "Dateiformatfehler",
                "text": "Dateiformat muss *.xlsx oder *.xls sein"
            },
            {
                "item": "error_201",
                "title": "Zusammensetzungsfehler",
                "text": "Das Flurstückskennzeichen wurde nicht korrekt eingesetzt. Bitte überprüfen sie die Exceldatei"
            },
            {
                "item": "error_211",
                "title": "API-Fehler",
                "text": "Problem bei der API-Abfrage (Status 400). Nähere Infos im Error-Log. Bitte wenden sie sich"
                        " an den Programmadministrator"
            },
            {
                "item": "error_212",
                "title": "API-Fehler",
                "text": "Problem bei der API-Abfrage (API-Status 404). Möglicherweise existiert mindestens ein"
                        " Flurstückkennzeichen nicht (z.B. wegen eines Tippfehlers). Nähere Infos im Error-Log. Bitte"
                        " wenden sie sich an den Programmadministrator"
            },
            {
                "item": "error_213",
                "title": "API-Fehler",
                "text": "Problem bei der API-Abfrage (API-Status 406). Nähere Infos im Error-Log. Bitte wenden sie sich"
                        " an den Programmadministrator"
            },
            {
                "item": "error_214",
                "title": "API-Fehler",
                "text": "Problem bei der API-Abfrage (API-Status 500). Nähere Infos im Error-Log. Bitte wenden sie sich"
                        " an den Programmadministrator"
            }
        ]
}

with open('settings.json', 'w') as file:
    json.dump(settings, file)
