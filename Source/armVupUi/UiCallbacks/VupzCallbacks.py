from Source.armVupUi.UiEntity.InfWidget import InfWidget
import tkinter as tk


def create_inf(main_w, vupz_obj):
    InfWidget(main_w, vupz_obj).place(relx=0.1, rely=0.5, anchor=tk.CENTER)
