import tkinter as tk
from Src.armVupLogic.VupzLogic import TP
from Src.armVupUi.UiEntity.VupzWidget import ArmVupzWidget


class ArmMainwindow(tk.Tk):
    def __init__(self, tp: TP):
        super().__init__()
        self.tp = tp
        self.title('Main Window')
        self.geometry("1980x1024")
        self.tp_start_pos = (200, 500)

    def create_context(self):
        self.vupz_wigets = []
        y_coord = self.tp_start_pos[0]
        x_coord = self.tp_start_pos[1]
        for way in self.tp.ways:
            for vupz in way.vupz_obj:
                vupz_window = ArmVupzWidget(self, vupz)
                vupz_window.place(x=x_coord, y=y_coord)
                x_coord += vupz_window.w_size[0] + 10
                self.vupz_wigets.append(vupz_window)
            x_coord = self.tp_start_pos[1]
            y_coord += vupz_window.w_size[1]
