import customtkinter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from src.models.pcb import PCB


class Gantt(customtkinter.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.fig, self.chart = plt.subplots()
        self.chart.set_ylim(0, 50)
        self.chart.set_xticks([])


        self.y_space = 0
        self.x_control = 0
        self.process_name_list = []
        self.process_y_list = []

        self.chart.grid(False)


        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        canvas_widget = self.canvas.get_tk_widget()
        canvas_widget.grid(row=0, column=0, sticky="nsew")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)


    def plot_execution_bar(self, process: PCB):
        index = self.process_name_list.index(process.name)
        y = self.process_y_list[index]

        self.chart.broken_barh(
            [(self.x_control, self.x_control+1)], (y-3/2, 3), facecolors=('tab:green'))
        self.update_view()

    def plot_stop_bar(self, process: PCB):
        index = self.process_name_list.index(process.name)
        y = self.process_y_list[index]

        self.chart.broken_barh(
            [(self.x_control, self.x_control+1)], (y-3/2, 3), facecolors=('tab:red'))
        self.update_view()

    def add_process(self, process: PCB):
        self.y_space = self.y_space+5
        self.process_name_list.append(process.name)
        self.process_y_list.append(self.y_space)
        self.chart.set_yticks(self.process_y_list)
        self.chart.set_yticklabels(self.process_name_list)

    def update_view(self):
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        canvas_widget = self.canvas.get_tk_widget()
        canvas_widget.grid(row=0, column=0, sticky="nsew")
