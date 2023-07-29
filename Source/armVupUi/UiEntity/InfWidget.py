import tkinter as tk


class InfWidget(tk.Frame):
    def __init__(self, main_w, vupz_obj):
        self.vupz_obj = vupz_obj
        self.w_size = (200, 500)
        super().__init__(main_w,
                         width=self.w_size[0],
                         height=self.w_size[1],
                         highlightbackground="black",
                         highlightthickness=2)
        self.table = InfTable(self, [['СТП5', 'kek'],
                                     ['kek', 'lol']])


class InfTable:
    def __init__(self, frame, data_for_table):
        total_rows = len(data_for_table)
        total_columns = len(data_for_table[0])
        self.lable = tk.Label(frame, text=f'Параметры {data_for_table[0][0]}',
                              font=('Arial', 12, 'bold'), justify='center')
        self.lable.grid(row=0, columnspan=2)
        for i in range(total_rows):
            for j in range(total_columns):
                e = tk.Label(frame, width=20, fg='black',
                             font=('Arial', 12), justify='center',
                             text=data_for_table[i][j])
                e.grid(row=i+1, column=j)
