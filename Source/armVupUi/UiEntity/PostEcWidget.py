import tkinter as tk


class PostWiget(tk.Frame):
    def __init__(self, main_w):
        self.w_size = (300, 100)
        super().__init__(main_w,
                         width=self.w_size[0],
                         height=self.w_size[1])
        self.configure(bg='')
        self.canvas = tk.Canvas(self,
                                height=self.w_size[1],
                                width=self.w_size[0])
        self.canvas.create_rectangle(1, 1,
                                     self.w_size[0],
                                     self.w_size[1],
                                     outlineoffset='center',
                                     width=4)
        self.canvas.place(relx=0, rely=0)
        self.post_lable = tk.Label(self, text='ПОСТ ЭЦ')
        self.post_lable.place(relx=0.5,
                              rely=0.5,
                              anchor=tk.CENTER)
