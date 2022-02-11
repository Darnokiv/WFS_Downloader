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
        self.root_window.title(f"GIS Downloader")
        self.root_window.geometry("900x600+40+40")
        self.root_window.resizable(False, False)
        self.frm_main = tk.Frame()
        self.root_gui()
        self.root_window.mainloop()

    def root_gui(self):

        self.frm_main = tk.Frame(
            master=self.root_window
        )
        lbl_welcome = tk.Label(
            master=self.frm_main,
            font="Helvetica 30 bold",
            text="GIS Downloader"
        )
        btn_variante1 = tk.Button(
            master=self.frm_main,
            width=45,
            height=9,
            font=20,
            text="Variante 1"
        )
        btn_variante2 = tk.Button(
            master=self.frm_main,
            width=45,
            height=9,
            font=20,
            text="Variante 2"
        )
        btn_variante3 = tk.Button(
            master=self.frm_main,
            width=45,
            height=9,
            font=20,
            text="Variante 3"
        )
        btn_variante4 = tk.Button(
            master=self.frm_main,
            width=45,
            height=9,
            font=20,
            text="Variante 4"
        )

        self.frm_main.grid(
            column=0, row=0
        )
        lbl_welcome.grid(
            column=2, row=0, columnspan=10, rowspan=2, padx=300, pady=40
        )
        btn_variante1.grid(
            column=2, row=2, padx=20, pady=30
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
