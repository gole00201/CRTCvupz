import tkinter as tk


class ArmVupzWindow(tk.Toplevel):
    def __init__(self, main_window, vupz_object):
        super().__init__(main_window)
        self.geometry("100x100")
        self.attributes('-alpha', 0.5)
        self.attributes('-topmost', True)
        self.overrideredirect(True)
        self.config(menu=tk.Menu(self))
        self.vupz_object = vupz_object
        self.label = tk.Label(self, text=self.vupz_object.name)
        self.label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
