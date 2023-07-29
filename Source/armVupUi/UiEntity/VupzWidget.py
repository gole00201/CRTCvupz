import tkinter as tk
from Source.armVupLogic.VupzLogic import VupzObjectClass
from Source.armVupUi.UiCallbacks.VupzCallbacks import create_inf


class ArmVupzWidget(tk.Frame):
    def __init__(self, main_window, vupz_object: VupzObjectClass):
        self.w_size = (300, 130)
        self.vupz_rec_size = (20, 10)
        self.vupz_obj = vupz_object
        super().__init__(main_window,
                         width=self.w_size[0],
                         height=self.w_size[1])
        self.configure(bg='')
        self.canvas = tk.Canvas(self, height=self.w_size[1],
                                width=self.w_size[0])
        self.canvas.place(relx=0, rely=0)
        ln = self.canvas.create_line(0, self.w_size[1]//2,
                                     self.w_size[0], self.w_size[1]//2,
                                     width=3, fill="black")
        self.vupz_way = ln
        ln = self.canvas.create_line(self.w_size[0]//2 - self.vupz_rec_size[0],
                                     self.w_size[1]//2 + self.vupz_rec_size[1],
                                     self.w_size[0]//2 + self.vupz_rec_size[0],
                                     self.w_size[1]//2 + self.vupz_rec_size[1],
                                     width=15,
                                     fill='blue')
        self.vupz_line = ln
        self.label = tk.Label(self, text=vupz_object.name)
        self.inf_button = tk.Button(self, text='ИНФ',
                                    command=lambda: create_inf(main_window,
                                                               vupz_object))
        self.inf_button.place(relx=0, rely=0)
        self.plot_button = tk.Button(self, text='ДАВЛ')
        self.plot_button.place(relx=0.77, rely=0)
        self.errors_button = tk.Button(self, text='ОШИБ')
        self.errors_button.place(relx=0.375, rely=0)
        self.label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
