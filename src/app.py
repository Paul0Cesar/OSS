import tkinter
import tkinter.messagebox
import customtkinter
import signal
from src.views.simulation import Simulation
from src.utils.constants import *


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title(PROGRAM_NAME)
        self.geometry(f"{1100}x{580}")
        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.tabview = customtkinter.CTkTabview(self,fg_color="white")
        self.tabview.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.tabview.add("SO Settings")
        self.tabview.add("Processes")
        self.tabview.add(SIMULATION_LABEL)

        self.tabview.tab(SIMULATION_LABEL).grid_columnconfigure(1, weight=1)
        self.tabview.tab(SIMULATION_LABEL).grid_columnconfigure((2, 3), weight=0)
        self.tabview.tab(SIMULATION_LABEL).grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
    

        self.simulation_frame = Simulation(master=self.tabview.tab(SIMULATION_LABEL))

        self.protocol('WM_DELETE_WINDOW', self.quit)
        self.bind('<Control-q>', self.quit)
        signal.signal(signal.SIGINT, self.quit)

    def quit(self):
        super().quit()
