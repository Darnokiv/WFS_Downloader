import tkinter as tk


class RootWindow:
    """
    Creates the root window and its contents to be shown
    """

    def __init__(self):
        """
        Creates the root window

        Parameter
        ---------
        None

        Returns
        -------
        None
        """

        self.root_window = tk.Tk()
        self.root_window.title(f"GIS Downloader - Stiftung Rheinische Kulturlandschaft (Nur Intern verwenden)")
        self.root_window.geometry("900x600+120+120")
        self.root_window.resizable(False, False)
        self.root_window.iconphoto(True, tk.PhotoImage(file="srk_logo.png"))
        self.root_window.tk_setPalette(background="#97c11f")
        self.frm_main = tk.Frame()
        self.root_gui()
        self.root_window.mainloop()

    def root_gui(self):
        self.frm_main.destroy()

        self.frm_main = tk.Frame(
            master=self.root_window
        )
        lbl_welcome = tk.Label(
            master=self.frm_main,
            font="Bahnschrift 30",
            text="GIS Downloader"
        )
        btn_variante1 = tk.Button(
            master=self.frm_main,
            bg="#afd4f1",
            activebackground="#afd4f1",
            width=37,
            height=8,
            font="Bahnschrift 15",
            text="Variante 1"
        )
        btn_variante2 = tk.Button(
            master=self.frm_main,
            bg="#afd4f1",
            activebackground="#afd4f1",
            width=37,
            height=8,
            font="Bahnschrift 15",
            text="Variante 2"
        )
        btn_variante3 = tk.Button(
            master=self.frm_main,
            bg="#afd4f1",
            activebackground="#afd4f1",
            width=37,
            height=8,
            font="Bahnschrift 15",
            text="Variante 3"
        )
        btn_variante4 = tk.Button(
            master=self.frm_main,
            bg="#afd4f1",
            activebackground="#afd4f1",
            width=37,
            height=8,
            font="Bahnschrift 15",
            text="Variante 4"
        )

        self.frm_main.grid(
            column=0, row=0
        )
        lbl_welcome.grid(
            column=2, row=0, columnspan=10, rowspan=2, padx=300, pady=35
        )
        btn_variante1.grid(
            column=2, row=2, padx=20, pady=20
        )
        btn_variante2.grid(
            column=3, row=2
        )
        btn_variante3.grid(
            column=2, row=3
        )
        btn_variante4.grid(
            column=3, row=3
        )


RootWindow()
