import tkinter as tk
from Source.armVupLogic.VupzLogic import TP
from Source.armVupUi.UiEntity.VupzWidget import ArmVupzWidget
from Source.armVupUi.UiEntity.PostEcWidget import PostWiget


class ArmMainwindow(tk.Tk):
    def __init__(self, tp: TP):
        super().__init__()
        self.tp = tp
        self.title('Main Window')
        self.geometry("1980x1024")
        self.inf_window = None
        self.tp_start_pos = (200, 500)

    def create_context(self):
        self.vupz_wigets = []
        y_coord = self.tp_start_pos[0]
        x_coord = self.tp_start_pos[1]
        self.post_ec = PostWiget(self)
        post = self.tp.post_ec
        self.post_ec.place(x=post.relx * 1980,
                           y=post.rely * 1024)
        for way in self.tp.ways:
            for vupz in way.vupz_obj:
                vupz_window = ArmVupzWidget(self, vupz)
                vupz_window.place(x=x_coord, y=y_coord)
                x_coord += vupz_window.w_size[0] + 10
                self.vupz_wigets.append(vupz_window)
            x_coord = self.tp_start_pos[1]
            y_coord += vupz_window.w_size[1]

    def delete_thirst_inf_subwindow(self):
        if not self.inf_window:
            self.inf_window.destroy()
            self.inf_window = None
