import json
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


class RootWindow:
    """
    Creates the root window and its contents to be shown.
    Needs "bin/settings.json" file
    """

    def __init__(self):
        """
        Creates the root window and calls the GUI functions in this class

        @param self
        """

        self.root_window = tk.Tk()
        self.root_window.title(
            f"""{Settings().get_main("program_name", "program_name")} - 
{Settings().get_main("window_title", "window_title")}"""
        )
        self.root_window.geometry(Settings().get_main("geometry", "geometry"))
        self.root_window.resizable(True, True)
        self.root_window.minsize(600, 400)
        self.root_window.iconphoto(True, tk.PhotoImage(file=Settings().get_main("icon", "icon")))
        self.root_window.tk_setPalette(background=Settings().get_color("standard", "background"))
        self.frm_main = tk.Frame()
        self.root_gui()
        self.root_window.mainloop()

    def root_gui(self):
        """
        Creates the GUI of the root window and
        the buttons to choose the variant

        @param self
        """
        self.frm_main.destroy()

        self.frm_main = tk.Frame(
            master=self.root_window
        )

        frm_title = tk.Frame(
            master=self.frm_main
        )
        lbl_welcome = tk.Label(
            master=frm_title,
            font=Settings().get_font("big"),
            text=Settings().get_main("program_name", "program_name")
        )

        frm_buttons = tk.Frame(
            master=self.frm_main
        )
        btn_variante1 = tk.Button(
            master=frm_buttons,
            background=Settings().get_color("button", "background"),
            activebackground=Settings().get_color("button", "activebackground"),
            font=Settings().get_font("normal"),
            text=Settings().get_text("variant_1"),
            command=lambda: [self.frm_main.destroy(), Variante1(self.root_window)]
        )
        btn_variante2 = tk.Button(
            master=frm_buttons,
            background=Settings().get_color("button", "background"),
            activebackground=Settings().get_color("button", "activebackground"),
            font=Settings().get_font("normal"),
            text=Settings().get_text("variant_2"),
            command=lambda: [self.frm_main.destroy(), Variante2(self.root_window)]
        )
        btn_variante3 = tk.Button(
            master=frm_buttons,
            background=Settings().get_color("button", "background"),
            activebackground=Settings().get_color("button", "activebackground"),
            font=Settings().get_font("normal"),
            text=Settings().get_text("variant_3"),
            command=lambda: [self.frm_main.destroy(), Variante3(self.root_window)]
        )
        btn_variante4 = tk.Button(
            master=frm_buttons,
            background=Settings().get_color("button", "background"),
            activebackground=Settings().get_color("button", "activebackground"),
            font=Settings().get_font("normal"),
            text=Settings().get_text("variant_4"),
            command=lambda: [self.frm_main.destroy(), Variante4(self.root_window)]
        )

        self.frm_main.place(
            relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center"
        )

        frm_title.place(
            relx=0.5, rely=0.02, relwidth=1, relheight=0.1, anchor="n"
        )
        lbl_welcome.place(
            relx=0, rely=0, relwidth=1, relheight=1
        )

        frm_buttons.place(
            relx=0.5, rely=0.55, relwidth=0.9, relheight=0.8, anchor="center"
        )
        btn_variante1.place(
            relx=0, rely=0, relwidth=0.49, relheight=0.49, anchor="nw"
        )
        btn_variante2.place(
            relx=1, rely=0, relwidth=0.49, relheight=0.49, anchor="ne"
        )
        btn_variante3.place(
            relx=0, rely=1, relwidth=0.49, relheight=0.49, anchor="sw"
        )
        btn_variante4.place(
            relx=1, rely=1, relwidth=0.49, relheight=0.49, anchor="se"
        )


class Variante1(RootWindow):
    """
    Creates the GUI for variant 1 and calls the needed functions to execute

    Subclass of "RootWindow"
    """

    def __init__(self, root_window):
        """
        Calls the GUI functions in this class

        @param root_window
        """

        super(RootWindow).__init__()

        self.root_window = root_window
        self.ent_source = None
        self.ent_target = None
        self.title_gui()
        self.selection_gui()
        self.start_gui()
        self.root_window.mainloop()

    def title_gui(self):
        """
        Creates the main frame and
        the title bar (Title and Back-Button)
        """

        self.frm_main = tk.Frame(
            master=self.root_window
        )

        frm_title = tk.Frame(
            master=self.frm_main
        )
        lbl_welcome = tk.Label(
            master=frm_title,
            font=Settings().get_font("big"),
            text=Settings().get_text("variant_1")
        )

        btn_back = tk.Button(
            master=self.frm_main,
            background=Settings().get_color("back_button", "background"),
            activebackground=Settings().get_color("back_button", "activebackground"),
            font=Settings().get_font("small"),
            text=Settings().get_text("back_button"),
            command=lambda: [self.frm_main.destroy(), RootWindow.root_gui(self)]
        )

        self.frm_main.place(
            relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center"
        )

        frm_title.place(
            relx=0.5, rely=0.05, relwidth=1, relheight=0.1, anchor="n"
        )
        lbl_welcome.place(
            relx=0, rely=0, relwidth=1, relheight=1
        )

        btn_back.place(
            x=10, y=10, relwidth=0.1, relheight=0.1
        )

    def selection_gui(self):
        """
        Creates the GUI to choose the source filepath and
        the target directory path
        """
        frm_fileselection = tk.Frame(
            master=self.frm_main
        )

        frm_source = tk.Frame(
            master=frm_fileselection,
            relief=Settings().get_relief("file_frame"),
            borderwidth=Settings().get_size("relief", "borderwidth")
        )
        lbl_open = tk.Label(
            master=frm_source,
            font=Settings().get_font("normal_underlined"),
            text=Settings().get_text("source_title_label")
        )
        lbl_source = tk.Label(
            master=frm_source,
            font=Settings().get_font("small"),
            text=Settings().get_text("source_entry_label")
        )
        self.ent_source = tk.Entry(
            master=frm_source,
            background=Settings().get_color("entry", "background"),
            selectbackground=Settings().get_color("entry", "selectbackground"),
            selectforeground=Settings().get_color("entry", "selectforeground"),
            font=Settings().get_font("small"),
        )
        btn_open = tk.Button(
            master=frm_source,
            background=Settings().get_color("button", "background"),
            activebackground=Settings().get_color("button", "activebackground"),
            font=Settings().get_font("small"),
            text=Settings().get_text("explorer_button"),
            command=lambda: [self.open_file()]
        )

        frm_target = tk.Frame(
            master=frm_fileselection,
            relief=Settings().get_relief("file_frame"),
            borderwidth=Settings().get_size("relief", "borderwidth")
        )
        lbl_save = tk.Label(
            master=frm_target,
            font=Settings().get_font("normal_underlined"),
            text=Settings().get_text("target_title_label")
        )
        lbl_target = tk.Label(
            master=frm_target,
            font=Settings().get_font("small"),
            text=Settings().get_text("target_entry_label")
        )
        self.ent_target = tk.Entry(
            master=frm_target,
            background=Settings().get_color("entry", "background"),
            selectbackground=Settings().get_color("entry", "selectbackground"),
            selectforeground=Settings().get_color("entry", "selectforeground"),
            font=Settings().get_font("small"),
        )
        btn_save = tk.Button(
            master=frm_target,
            background=Settings().get_color("button", "background"),
            activebackground=Settings().get_color("button", "activebackground"),
            font=Settings().get_font("small"),
            text=Settings().get_text("explorer_button"),
            command=lambda: [self.save_file()]
        )

        frm_fileselection.place(
            relx=0.5, rely=0.5, relwidth=0.85, relheight=0.5, anchor="center"
        )

        frm_source.place(
            relx=0, rely=0, relwidth=1, relheight=0.45, anchor="nw"
        )
        lbl_open.place(
            relx=0.01, rely=0.1, relwidth=0.2, relheight=0.2, anchor="nw"
        )
        lbl_source.place(
            relx=0.01, rely=0.5, relwidth=0.2, relheight=0.2, anchor="w"
        )
        self.ent_source.place(
            relx=0.99, rely=0.5, relwidth=0.79, height=25, anchor="e"
        )
        btn_open.place(
            relx=0.01, rely=0.9, relwidth=0.2, relheight=0.2, anchor="sw"
        )

        frm_target.place(
            relx=0, rely=1, relwidth=1, relheight=0.45, anchor="sw"
        )
        lbl_save.place(
            relx=0.01, rely=0.1, relwidth=0.2, relheight=0.2, anchor="nw"
        )
        lbl_target.place(
            relx=0.01, rely=0.5, relwidth=0.2, relheight=0.2, anchor="w"
        )
        self.ent_target.place(
            relx=0.99, rely=0.5, relwidth=0.79, height=25, anchor="e"
        )
        btn_save.place(
            relx=0.01, rely=0.9, relwidth=0.2, relheight=0.2, anchor="sw"
        )

    def start_gui(self):
        """
        Creates the button to call "start()"
        """

        btn_start = tk.Button(
            master=self.frm_main,
            background=Settings().get_color("button", "background"),
            activebackground=Settings().get_color("button", "activebackground"),
            font=Settings().get_font("normal"),
            text=Settings().get_text("start_button"),
            command=lambda: [self.start()]
        )

        btn_start.place(
            relx=0.99, rely=0.99, relwidth=0.2, relheight=0.2, anchor="se"
        )

    def open_file(self):
        """
        Function to choose the source file.

        Opens the Explorer to select a file,
        clears "self.ent_target" and
        inserts the selected directory into "self.ent_target"
        """
        source = tk.filedialog.askopenfilename(filetypes=[("Excel files", ".xlsx .xls")])
        self.ent_source.delete(0, tk.END)
        self.ent_source.insert(0, source)

    def save_file(self):
        """
        Function to choose the save directory.

        Opens the Explorer to select a directory,
        clears "self.ent_target" and
        inserts the selected directory into "self.ent_target"
        """
        target = tk.filedialog.askdirectory()
        self.ent_target.delete(0, tk.END)
        self.ent_target.insert(0, target)

    def start(self):
        """
        Starts the main process.

        Gets the strings in "self.ent_source" and "self.ent_target",
        assigns these strings to the respective variables "source" and "target",
        checks if there are errors (gives an error message if necessary) and
        calls the main process.
        """
        # Parameters for function
        # Puts the paths into the variables
        source = self.ent_source.get()
        target = self.ent_target.get()

        s = os.path.isfile(source)
        t = os.path.isdir(target)

        if s is False and t is True:
            tk.messagebox.showerror(Settings().get_error("error_101", "title"),
                                    Settings().get_error("error_101", "text"))
        elif s is False and t is False:
            tk.messagebox.showerror(Settings().get_error("error_103", "title"),
                                    Settings().get_error("error_103", "text"))

        elif not os.path.splitext(source)[-1].lower() == ".xlsx" or os.path.splitext(source)[-1].lower() == ".xls":
            tk.messagebox.showerror(Settings().get_error("error_111", "title"),
                                    Settings().get_error("error_111", "text"))
        elif s is True and t is False:
            tk.messagebox.showerror(Settings().get_error("error_102", "title"),
                                    Settings().get_error("error_102", "text"))
        else:
            # function to be executed
            tk.messagebox.showinfo("In Arbeit", "In Arbeit")


class Variante2(RootWindow):
    """
    Creates the GUI for variant 2 and calls the needed functions to execute

    Subclass of "RootWindow"
    """

    def __init__(self, root_window):
        """
        Calls the GUI functions in this class

        @param root_window
        """
        super(RootWindow).__init__()

        self.ent_target = None

        self.root_window = root_window
        self.title_gui()
        self.selection_gui()
        self.start_gui()
        self.root_window.mainloop()

    def title_gui(self):
        """
        Creates the main frame and
        the title bar (Title and Back-Button)
        """

        self.frm_main = tk.Frame(
            master=self.root_window
        )

        frm_title = tk.Frame(
            master=self.frm_main
        )
        lbl_welcome = tk.Label(
            master=frm_title,
            font=Settings().get_font("big"),
            text=Settings().get_text("variant_2")
        )

        btn_back = tk.Button(
            master=self.frm_main,
            background=Settings().get_color("back_button", "background"),
            activebackground=Settings().get_color("back_button", "activebackground"),
            font=Settings().get_font("small"),
            text=Settings().get_text("back_button"),
            command=lambda: [self.frm_main.destroy(), RootWindow.root_gui(self)]
        )

        self.frm_main.place(
            relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center"
        )

        frm_title.place(
            relx=0.5, rely=0.05, relwidth=1, relheight=0.1, anchor="n"
        )
        lbl_welcome.place(
            relx=0, rely=0, relwidth=1, relheight=1
        )

        btn_back.place(
            x=10, y=10, relwidth=0.1, relheight=0.1
        )

    def selection_gui(self):
        """
        Creates the GUI to choose the target directory path
        """
        frm_fileselection = tk.Frame(
            master=self.frm_main
        )

        frm_source = tk.Frame(
            master=frm_fileselection,
            relief=Settings().get_relief("file_frame"),
            borderwidth=Settings().get_size("relief", "borderwidth")
        )

        frm_target = tk.Frame(
            master=frm_fileselection,
            relief=Settings().get_relief("file_frame"),
            borderwidth=Settings().get_size("relief", "borderwidth")
        )
        lbl_save = tk.Label(
            master=frm_target,
            font=Settings().get_font("normal_underlined"),
            text=Settings().get_text("target_title_label")
        )
        lbl_target = tk.Label(
            master=frm_target,
            font=Settings().get_font("small"),
            text=Settings().get_text("target_entry_label")
        )
        self.ent_target = tk.Entry(
            master=frm_target,
            background=Settings().get_color("entry", "background"),
            selectbackground=Settings().get_color("entry", "selectbackground"),
            selectforeground=Settings().get_color("entry", "selectforeground"),
            font=Settings().get_font("small"),
        )
        btn_save = tk.Button(
            master=frm_target,
            background=Settings().get_color("button", "background"),
            activebackground=Settings().get_color("button", "activebackground"),
            font=Settings().get_font("small"),
            text=Settings().get_text("explorer_button"),
            command=lambda: [self.save_file()]
        )

        frm_fileselection.place(
            relx=0.5, rely=0.5, relwidth=0.85, relheight=0.5, anchor="center"
        )

        frm_source.place(
            relx=0, rely=0, relwidth=1, relheight=0.45, anchor="nw"
        )

        frm_target.place(
            relx=0, rely=1, relwidth=1, relheight=0.45, anchor="sw"
        )
        lbl_save.place(
            relx=0.01, rely=0.1, relwidth=0.2, relheight=0.2, anchor="nw"
        )
        lbl_target.place(
            relx=0.01, rely=0.5, relwidth=0.2, relheight=0.2, anchor="w"
        )
        self.ent_target.place(
            relx=0.99, rely=0.5, relwidth=0.79, height=25, anchor="e"
        )
        btn_save.place(
            relx=0.01, rely=0.9, relwidth=0.2, relheight=0.2, anchor="sw"
        )

    def start_gui(self):
        """
        Creates the button to call "start()"
        """

        btn_start = tk.Button(
            master=self.frm_main,
            background=Settings().get_color("button", "background"),
            activebackground=Settings().get_color("button", "activebackground"),
            font=Settings().get_font("normal"),
            text=Settings().get_text("start_button"),
            command=lambda: [self.start()]
        )

        btn_start.place(
            relx=0.99, rely=0.99, relwidth=0.2, relheight=0.2, anchor="se"
        )

    def save_file(self):
        """
        Function to choose the save directory.

        Opens the Explorer to select a directory,
        clears "self.ent_target" and
        inserts the selected directory into "self.ent_target"
        """
        target = tk.filedialog.askdirectory()
        self.ent_target.delete(0, tk.END)
        self.ent_target.insert(0, target)

    def start(self):
        """
        Starts the main process.

        Gets the string "self.ent_target",
        assigns this string to the variable "target",
        checks if there are errors (gives an error message if necessary) and
        calls the main process.
        """
        # Parameters for function
        # Puts the path into the variable
        target = self.ent_target.get()

        t = os.path.isdir(target)

        if t is False:
            tk.messagebox.showerror(Settings().get_error("error_102", "title"),
                                    Settings().get_error("error_102", "text"))
        else:
            # function to be executed
            tk.messagebox.showinfo("In Arbeit", "In Arbeit")


class Variante3(RootWindow):
    """
    Creates the GUI for variant 3 and calls the needed functions to execute

    Subclass of "RootWindow"
    """

    def __init__(self, root_window):
        """
        Calls the GUI functions in this class

        @param root_window
        """
        super(RootWindow).__init__()

        self.ent_target = None

        self.root_window = root_window
        self.title_gui()
        self.selection_gui()
        self.start_gui()
        self.root_window.mainloop()

    def title_gui(self):
        """
        Creates the main frame and
        the title bar (Title and Back-Button)
        """

        self.frm_main = tk.Frame(
            master=self.root_window
        )

        frm_title = tk.Frame(
            master=self.frm_main
        )
        lbl_welcome = tk.Label(
            master=frm_title,
            font=Settings().get_font("big"),
            text=Settings().get_text("variant_3")
        )

        btn_back = tk.Button(
            master=self.frm_main,
            background=Settings().get_color("back_button", "background"),
            activebackground=Settings().get_color("back_button", "activebackground"),
            font=Settings().get_font("small"),
            text=Settings().get_text("back_button"),
            command=lambda: [self.frm_main.destroy(), RootWindow.root_gui(self)]
        )

        self.frm_main.place(
            relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center"
        )

        frm_title.place(
            relx=0.5, rely=0.05, relwidth=1, relheight=0.1, anchor="n"
        )
        lbl_welcome.place(
            relx=0, rely=0, relwidth=1, relheight=1
        )

        btn_back.place(
            x=10, y=10, relwidth=0.1, relheight=0.1
        )

    def selection_gui(self):
        """
        Creates the GUI to choose the target directory path
        """
        frm_fileselection = tk.Frame(
            master=self.frm_main
        )

        frm_source = tk.Frame(
            master=frm_fileselection,
            relief=Settings().get_relief("file_frame"),
            borderwidth=Settings().get_size("relief", "borderwidth")
        )

        frm_target = tk.Frame(
            master=frm_fileselection,
            relief=Settings().get_relief("file_frame"),
            borderwidth=Settings().get_size("relief", "borderwidth")
        )
        lbl_save = tk.Label(
            master=frm_target,
            font=Settings().get_font("normal_underlined"),
            text=Settings().get_text("target_title_label")
        )
        lbl_target = tk.Label(
            master=frm_target,
            font=Settings().get_font("small"),
            text=Settings().get_text("target_entry_label")
        )
        self.ent_target = tk.Entry(
            master=frm_target,
            background=Settings().get_color("entry", "background"),
            selectbackground=Settings().get_color("entry", "selectbackground"),
            selectforeground=Settings().get_color("entry", "selectforeground"),
            font=Settings().get_font("small"),
        )
        btn_save = tk.Button(
            master=frm_target,
            background=Settings().get_color("button", "background"),
            activebackground=Settings().get_color("button", "activebackground"),
            font=Settings().get_font("small"),
            text=Settings().get_text("explorer_button"),
            command=lambda: [self.save_file()]
        )

        frm_fileselection.place(
            relx=0.5, rely=0.5, relwidth=0.85, relheight=0.5, anchor="center"
        )

        frm_source.place(
            relx=0, rely=0, relwidth=1, relheight=0.45, anchor="nw"
        )

        frm_target.place(
            relx=0, rely=1, relwidth=1, relheight=0.45, anchor="sw"
        )
        lbl_save.place(
            relx=0.01, rely=0.1, relwidth=0.2, relheight=0.2, anchor="nw"
        )
        lbl_target.place(
            relx=0.01, rely=0.5, relwidth=0.2, relheight=0.2, anchor="w"
        )
        self.ent_target.place(
            relx=0.99, rely=0.5, relwidth=0.79, height=25, anchor="e"
        )
        btn_save.place(
            relx=0.01, rely=0.9, relwidth=0.2, relheight=0.2, anchor="sw"
        )

    def start_gui(self):
        """
        Creates the button to call "start()"
        """

        btn_start = tk.Button(
            master=self.frm_main,
            background=Settings().get_color("button", "background"),
            activebackground=Settings().get_color("button", "activebackground"),
            font=Settings().get_font("normal"),
            text=Settings().get_text("start_button"),
            command=lambda: [self.start()]
        )

        btn_start.place(
            relx=0.99, rely=0.99, relwidth=0.2, relheight=0.2, anchor="se"
        )

    def save_file(self):
        """
        Function to choose the save directory.

        Opens the Explorer to select a directory,
        clears "self.ent_target" and
        inserts the selected directory into "self.ent_target"
        """
        target = tk.filedialog.askdirectory()
        self.ent_target.delete(0, tk.END)
        self.ent_target.insert(0, target)

    def start(self):
        """
        Starts the main process.

        Gets the string "self.ent_target",
        assigns this string to the variable "target",
        checks if there are errors (gives an error message if necessary) and
        calls the main process.
        """
        # Parameters for function
        # Puts the path into the variable
        target = self.ent_target.get()

        t = os.path.isdir(target)

        if t is False:
            tk.messagebox.showerror(Settings().get_error("error_102", "title"),
                                    Settings().get_error("error_102", "text"))
        else:
            # function to be executed
            tk.messagebox.showinfo("In Arbeit", "In Arbeit")


class Variante4(RootWindow):
    """
    Creates the GUI for variant 4 and calls the needed functions to execute

    Subclass of "RootWindow"
    """

    def __init__(self, root_window):
        """
        Calls the GUI functions in this class

        @param root_window
        """
        super(RootWindow).__init__()

        self.ent_target = None

        self.root_window = root_window
        self.title_gui()
        self.selection_gui()
        self.start_gui()
        self.root_window.mainloop()

    def title_gui(self):
        """
        Creates the main frame and
        the title bar (Title and Back-Button)
        """

        self.frm_main = tk.Frame(
            master=self.root_window
        )

        frm_title = tk.Frame(
            master=self.frm_main
        )
        lbl_welcome = tk.Label(
            master=frm_title,
            font=Settings().get_font("big"),
            text=Settings().get_text("variant_4")
        )

        btn_back = tk.Button(
            master=self.frm_main,
            background=Settings().get_color("back_button", "background"),
            activebackground=Settings().get_color("back_button", "activebackground"),
            font=Settings().get_font("small"),
            text=Settings().get_text("back_button"),
            command=lambda: [self.frm_main.destroy(), RootWindow.root_gui(self)]
        )

        self.frm_main.place(
            relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center"
        )

        frm_title.place(
            relx=0.5, rely=0.05, relwidth=1, relheight=0.1, anchor="n"
        )
        lbl_welcome.place(
            relx=0, rely=0, relwidth=1, relheight=1
        )

        btn_back.place(
            x=10, y=10, relwidth=0.1, relheight=0.1
        )

    def selection_gui(self):
        """
        Creates the GUI to choose the target directory path
        """
        frm_fileselection = tk.Frame(
            master=self.frm_main
        )

        frm_source = tk.Frame(
            master=frm_fileselection,
            relief=Settings().get_relief("file_frame"),
            borderwidth=Settings().get_size("relief", "borderwidth")
        )

        frm_target = tk.Frame(
            master=frm_fileselection,
            relief=Settings().get_relief("file_frame"),
            borderwidth=Settings().get_size("relief", "borderwidth")
        )
        lbl_save = tk.Label(
            master=frm_target,
            font=Settings().get_font("normal_underlined"),
            text=Settings().get_text("target_title_label")
        )
        lbl_target = tk.Label(
            master=frm_target,
            font=Settings().get_font("small"),
            text=Settings().get_text("target_entry_label")
        )
        self.ent_target = tk.Entry(
            master=frm_target,
            background=Settings().get_color("entry", "background"),
            selectbackground=Settings().get_color("entry", "selectbackground"),
            selectforeground=Settings().get_color("entry", "selectforeground"),
            font=Settings().get_font("small"),
        )
        btn_save = tk.Button(
            master=frm_target,
            background=Settings().get_color("button", "background"),
            activebackground=Settings().get_color("button", "activebackground"),
            font=Settings().get_font("small"),
            text=Settings().get_text("explorer_button"),
            command=lambda: [self.save_file()]
        )

        frm_fileselection.place(
            relx=0.5, rely=0.5, relwidth=0.85, relheight=0.5, anchor="center"
        )

        frm_source.place(
            relx=0, rely=0, relwidth=1, relheight=0.45, anchor="nw"
        )

        frm_target.place(
            relx=0, rely=1, relwidth=1, relheight=0.45, anchor="sw"
        )
        lbl_save.place(
            relx=0.01, rely=0.1, relwidth=0.2, relheight=0.2, anchor="nw"
        )
        lbl_target.place(
            relx=0.01, rely=0.5, relwidth=0.2, relheight=0.2, anchor="w"
        )
        self.ent_target.place(
            relx=0.99, rely=0.5, relwidth=0.79, height=25, anchor="e"
        )
        btn_save.place(
            relx=0.01, rely=0.9, relwidth=0.2, relheight=0.2, anchor="sw"
        )

    def start_gui(self):
        """
        Creates the button to call "start()"
        """

        btn_start = tk.Button(
            master=self.frm_main,
            background=Settings().get_color("button", "background"),
            activebackground=Settings().get_color("button", "activebackground"),
            font=Settings().get_font("normal"),
            text=Settings().get_text("start_button"),
            command=lambda: [self.start()]
        )

        btn_start.place(
            relx=0.99, rely=0.99, relwidth=0.2, relheight=0.2, anchor="se"
        )

    def save_file(self):
        """
        Function to choose the save directory.

        Opens the Explorer to select a directory,
        clears "self.ent_target" and
        inserts the selected directory into "self.ent_target"
        """
        target = tk.filedialog.askdirectory()
        self.ent_target.delete(0, tk.END)
        self.ent_target.insert(0, target)

    def start(self):
        """
        Starts the main process.

        Gets the string "self.ent_target",
        assigns this string to the variable "target",
        checks if there are errors (gives an error message if necessary) and
        calls the main process.
        """
        # Parameters for function
        # Puts the path into the variable
        target = self.ent_target.get()

        t = os.path.isdir(target)

        if t is False:
            tk.messagebox.showerror(Settings().get_error("error_102", "title"),
                                    Settings().get_error("error_102", "text"))
        else:
            # function to be executed
            tk.messagebox.showinfo("In Arbeit", "In Arbeit")


class Settings:
    """
    Gets all settings from the "bin/settings.json" file
    """

    def __init__(self):
        """
        Opens the "bin/settings.json" file
        """

        with open('bin/settings.json', 'r') as file:
            self.settings_file = json.load(file)

    def get_main(self, item, parameter):
        """
        Gives settings from the main category

        :param item: item for which the information is needed (e.g. "program_title")
        :type item: str
        :param parameter: which information is needed (e.g. "program_title")
        :type parameter: str

        :return: value
        :rtype: str
        """

        value = None

        for group in self.settings_file["main"]:
            if group["item"] == item:
                value = group[parameter]
                break

        return value

    def get_color(self, item, parameter):
        """
        Gives settings from the color category

        :param item: item for which the color is needed (e.g. "button")
        :type item: str
        :param parameter: which color is needed (e.g. "background")
        :type parameter: str

        :return: value
        :rtype: str
        """

        value = None

        for group in self.settings_file["color"]:
            if group["item"] == item:
                value = group[parameter]
                break

        return value

    def get_font(self, item):
        """
        Gives settings from the font category

        :param item: size of the font (e.g. "small")
        :type item: str

        :return: value
        :rtype: str
        """

        value = None

        for group in self.settings_file["font"]:
            if group["item"] == item:
                value = group["font"]
                break

        return value

    def get_text(self, item):
        """
        Gives settings from the text category

        :param item: which text (e.g. "back_button")
        :type item: str

        :return: value
        :rtype: str
        """

        value = None

        for group in self.settings_file["text"]:
            if group["item"] == item:
                value = group["text"]
                break

        return value

    def get_size(self, item, parameter):
        """
        Gives settings from the size category

        :param item: item for which the size is needed (e.g. "back_button")
        :type item: str
        :param parameter: which size is needed (e.g. "width")
        :type parameter: str

        :return: value
        :rtype: int
        """

        value = None

        for group in self.settings_file["size"]:
            if group["item"] == item:
                value = group[parameter]
                break

        return value

    def get_relief(self, item):
        """
        Gives settings from the relief category

        :param item: item for which the relief is needed (e.g. "file_frame")
        :type item: str

        :return: value
        """

        value = None

        for group in self.settings_file["relief"]:
            if group["item"] == item:
                value = group["relief"]
                break

        return value

    def get_error(self, item, parameter):
        """
        Gives settings from the error category

        :param item: error ID (e.g. "error_101")
        :type item: str
        :param parameter: which information is needed (e.g. "text")
        :type parameter: str

        :return: value
        :rtype: str
        """

        value = None

        for group in self.settings_file["error"]:
            if group["item"] == item:
                value = group[parameter]
                break

        return value


RootWindow()
