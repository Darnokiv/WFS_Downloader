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
            text="Variante 1",
            command=lambda: [self.frm_main.destroy(), Variante1(self.root_window)]
        )
        btn_variante2 = tk.Button(
            master=self.frm_main,
            bg="#afd4f1",
            activebackground="#afd4f1",
            width=37,
            height=8,
            font="Bahnschrift 15",
            text="Variante 2",
            command=lambda: [self.frm_main.destroy(), Variante2(self.root_window)]
        )
        btn_variante3 = tk.Button(
            master=self.frm_main,
            bg="#afd4f1",
            activebackground="#afd4f1",
            width=37,
            height=8,
            font="Bahnschrift 15",
            text="Variante 3",
            command=lambda: [self.frm_main.destroy(), Variante3(self.root_window)]
        )
        btn_variante4 = tk.Button(
            master=self.frm_main,
            bg="#afd4f1",
            activebackground="#afd4f1",
            width=37,
            height=8,
            font="Bahnschrift 15",
            text="Variante 4",
            command=lambda: [self.frm_main.destroy(), Variante4(self.root_window)]
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


class Variante1(RootWindow):

    def __init__(self, root_window):
        super(RootWindow).__init__()

        self.root_window = root_window
        self.variante1_gui()
        self.root_window.mainloop()

    def variante1_gui(self):

        self.frm_main = tk.Frame(
            master=self.root_window
        )
        lbl_welcome = tk.Label(
            master=self.frm_main,
            font="Bahnschrift 30",
            text="Variante 1"
        )
        btn_back = tk.Button(
            master=self.frm_main,
            bg="#da5454",
            activebackground="white",
            width=10,
            height=3,
            font="Bahnschrift",
            text="Zurück",
            command=lambda: [self.frm_main.destroy(), RootWindow.root_gui(self)]
        )

        self.frm_main.grid(
            column=0, row=0
        )
        lbl_welcome.grid(
            column=2, row=0, columnspan=10, rowspan=2, padx=230, pady=35
        )
        btn_back.grid(
            column=1, row=0, padx=10
        )


class Variante2(RootWindow):

    def __init__(self, root_window):
        super(RootWindow).__init__()

        self.root_window = root_window
        self.variante2_gui()
        self.root_window.mainloop()

    def variante2_gui(self):

        self.frm_main = tk.Frame(
            master=self.root_window
        )
        lbl_welcome = tk.Label(
            master=self.frm_main,
            font="Bahnschrift 30",
            text="Variante 2"
        )
        btn_back = tk.Button(
            master=self.frm_main,
            bg="#da5454",
            activebackground="white",
            width=10,
            height=3,
            font="Bahnschrift",
            text="Zurück",
            command=lambda: [self.frm_main.destroy(), RootWindow.root_gui(self)]
        )

        self.frm_main.grid(
            column=0, row=0
        )
        lbl_welcome.grid(
            column=2, row=0, columnspan=10, rowspan=2, padx=230, pady=35
        )
        btn_back.grid(
            column=1, row=0, padx=10
        )


class Variante3(RootWindow):

    def __init__(self, root_window):
        super(RootWindow).__init__()

        self.root_window = root_window
        self.variante3_gui()
        self.root_window.mainloop()

    def variante3_gui(self):

        self.frm_main = tk.Frame(
            master=self.root_window
        )
        lbl_welcome = tk.Label(
            master=self.frm_main,
            font="Bahnschrift 30",
            text="Variante 3"
        )
        btn_back = tk.Button(
            master=self.frm_main,
            bg="#da5454",
            activebackground="white",
            width=10,
            height=3,
            font="Bahnschrift",
            text="Zurück",
            command=lambda: [self.frm_main.destroy(), RootWindow.root_gui(self)]
        )

        self.frm_main.grid(
            column=0, row=0
        )
        lbl_welcome.grid(
            column=2, row=0, columnspan=10, rowspan=2, padx=230, pady=35
        )
        btn_back.grid(
            column=1, row=0, padx=10
        )


class Variante4(RootWindow):

    def __init__(self, root_window):
        super(RootWindow).__init__()

        self.root_window = root_window
        self.variante4_gui()
        self.root_window.mainloop()

    def variante4_gui(self):

        self.frm_main = tk.Frame(
            master=self.root_window
        )
        lbl_welcome = tk.Label(
            master=self.frm_main,
            font="Bahnschrift 30",
            text="Variante 4"
        )
        btn_back = tk.Button(
            master=self.frm_main,
            bg="#da5454",
            activebackground="white",
            width=10,
            height=3,
            font="Bahnschrift",
            text="Zurück",
            command=lambda: [self.frm_main.destroy(), RootWindow.root_gui(self)]
        )

        self.frm_main.grid(
            column=0, row=0
        )
        lbl_welcome.grid(
            column=2, row=0, columnspan=10, rowspan=2, padx=230, pady=35
        )
        btn_back.grid(
            column=1, row=0, padx=10
        )


RootWindow()
