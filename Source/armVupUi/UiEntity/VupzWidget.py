import tkinter as tk
from Src.armVupLogic.VupzLogic import VupzObjectClass


class ArmVupzWidget(tk.Frame):
    def __init__(self, main_window, vupz_object: VupzObjectClass):
        self.w_size = (300, 100)
        super().__init__(main_window,
                         width=self.w_size[0],
                         height=self.w_size[1])
        self.configure(bg='')
        # self.button = tk.Button(self, text="Click Me")
        # self.button.pack(row=1, column=0, sticky="ew")
        self.canvas = tk.Canvas(self, height=self.w_size[1],
                                width=self.w_size[0])
        self.canvas.grid(row=2, column=0, sticky="ew")
        self.canvas.create_line(0, self.w_size[1]//2,
                                self.w_size[0], self.w_size[1]//2,
                                width=3, fill="black")
        self.label = tk.Label(self, text=vupz_object.name)
        self.label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.bind("<Configure>", self.on_canvas_resize)

    def on_canvas_resize(self, event):
        self.canvas.coords(self.canvas.find_all()[0],
                           0, event.height//2,
                           event.width, event.height//2)
