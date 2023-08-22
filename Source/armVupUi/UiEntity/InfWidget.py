import tkinter as tk


class InfWidget(tk.Frame):
    def __init__(self, main_w, vupz_obj):
        if main_w.inf_window:
            main_w.delete_thirst_inf_subwindow()
        self.vupz_obj = vupz_obj
        self.w_size = (300, 600)
        super().__init__(main_w,
                         width=self.w_size[0],
                         height=self.w_size[1],
                         highlightbackground="black",
                         highlightthickness=2)
        self.text = f'Состояние позиции {vupz_obj.name}'
        self.lable = tk.Label(self, text=self.text)
        self.lable.place(anchor=tk.CENTER, relx=0.5, rely=0.05)
        main_w.inf_window = self
