import tkinter as tk


class ArmMainwindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Main Window')
        self.geometry("1980x1024")
        self.mainloop()
