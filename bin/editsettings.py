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
                "window_title": "Stiftung Rheinische Kulturlandschaft (Nur Intern verwenden)"
            },
            {
                "item": "geometry",
                "geometry": "900x600+120+120"
            },
            {
                "item": "icon",
                "icon": "bin/srk_logo.png"
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
                "item": "variant_button",
                "width": 37,
                "height": 8
            },
            {
                "item": "back_button",
                "width": 10,
                "height": 3
            },
            {
                "item": "file_frame",
                "borderwidth": 2
            },
            {
                "item": "file_entry",
                "width": 78
            },
            {
                "item": "start_button",
                "width": 15,
                "height": 3
            }
        ],
    "relief":
        [
            {
                "item": "file_frame",
                "relief": "groove",
                "borderwidth": 2
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
            }
        ]
}

with open('settings.json', 'w') as file:
    json.dump(settings, file)