import tkinter
import tkinter.messagebox
import customtkinter
import signal
from src.views.simulation import Simulation
from src.views.processes import Processes
from src.utils.constants import *
from src.models.pcb import PCB
from src.models.page import Page

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

        self.pc1 = PCB(creation_time=0, PID=1, icon="src/resources/icons/chrome.png", name="chrome", total_time=20,
                       pages=[Page("01pg01"), Page("01pg02"), Page("01pg03")])
        self.pc2 = PCB(creation_time=2, PID=2, icon="src/resources/icons/terminal.png", name="terminal", total_time=16,
                       pages=[Page("02pg01"), Page("02pg02"), Page("02pg03")])
        self.pc3 = PCB(creation_time=3, PID=3, icon="src/resources/icons/visual-studio-code.png", name="vscode", total_time=10,
                       pages=[Page("03pg01"), Page("03pg02"), Page("03pg03")])

        self.process_list=[self.pc1,self.pc2,self.pc3]

        

        self.tabview = customtkinter.CTkTabview(self,fg_color="white")
        self.tabview.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        #self.tabview.add("SO Settings")
        self.tabview.add(PROCESSES_LABEL)
        self.tabview.add(SIMULATION_LABEL)

        self.tabview.tab(SIMULATION_LABEL).grid_columnconfigure(1, weight=1)
        self.tabview.tab(SIMULATION_LABEL).grid_columnconfigure((2, 3), weight=0)
        self.tabview.tab(SIMULATION_LABEL).grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

        self.tabview.tab(PROCESSES_LABEL).grid_columnconfigure((0, 1,2), weight=1)
        #self.tabview.tab(PROCESSES_LABEL).grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
    

        self.simulation_frame = Simulation(master=self.tabview.tab(SIMULATION_LABEL),process_list=self.process_list)
        self.processes_frame = Processes(master=self.tabview.tab(PROCESSES_LABEL),process_list=self.process_list)

        self.protocol('WM_DELETE_WINDOW', self.quit)
        self.bind('<Control-q>', self.quit)
        signal.signal(signal.SIGINT, self.quit)

    def quit(self):
        super().quit()
