import customtkinter
from src.widgets.process_list_frame import ProcessListFrame
from src.utils.constants import *
from src.models.pcb import PCB


class ProcessFrame(customtkinter.CTkFrame):

    def __init__(self, master,start_process, **kwargs):
        super().__init__(master, **kwargs)

        corner_radius = 12
        height = 30
        width = 250
        border_width = 2
        fg_color = "white"

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)
        self.grid_columnconfigure(3, weight=0)

        self.label = customtkinter.CTkLabel(self,text=PROCESS_RUNNING_LABEL,text_color="black")
        self.label.grid(row=0, column=0, padx=5)

        self.label = customtkinter.CTkLabel(self,text=PROCESS_READY_LABEL,text_color="black")
        self.label.grid(row=1, column=0, padx=5)

        self.label = customtkinter.CTkLabel(self,text=PROCECSS_BLOCKED_LABEL,text_color="black")
        self.label.grid(row=2, column=0, padx=5)

        self.label = customtkinter.CTkLabel(self,text=PROCESS_FINISHED_LABEL,text_color="black")
        self.label.grid(row=3, column=0, padx=5)

        self.label = customtkinter.CTkLabel(self,text=PROCESS_AVAILABLE_LABEL,wraplength=1,text_color="black")
        self.label.grid(row=0, column=3,rowspan=4, padx=5)

        self.process_running_frame = ProcessListFrame(
            master=self, fg_color=fg_color, width=width, height=height, corner_radius=corner_radius, border_width=border_width)
        self.process_running_frame.grid(
            row=0, column=1, padx=5, pady=10, sticky="nsew")
        #self.process_running_frame.mock_elements()

        self.process_ready_frame = ProcessListFrame(
            master=self, fg_color=fg_color, width=width, height=height, corner_radius=corner_radius, border_width=border_width)
        self.process_ready_frame.grid(
            row=1, column=1, padx=10, pady=10, sticky="nsew")
        #self.process_ready_frame.mock_elements()

        self.process_block_frame = ProcessListFrame(
            master=self, fg_color=fg_color, width=width, height=height, corner_radius=corner_radius, border_width=border_width)
        self.process_block_frame.grid(
            row=2, column=1, padx=10, pady=10, sticky="nsew")
        #self.process_block_frame.mock_elements()

        self.process_finish_frame = ProcessListFrame(
            master=self, fg_color=fg_color, width=width, height=height, corner_radius=corner_radius, border_width=border_width)
        self.process_finish_frame.grid(
            row=3, column=1, padx=10, pady=10, sticky="nsew")
        #self.process_finish_frame.mock_elements()

        self.process_available_frame = ProcessListFrame(
            master=self,start_process=start_process, orientation="vertical", fg_color=fg_color, width=height, height=width, corner_radius=corner_radius, border_width=border_width)
        self.process_available_frame.grid(
            row=0, column=2, rowspan=4, padx=10, pady=10)
        #self.process_available_frame.mock_elements()

    def update_process(self,process_running,process_ready,process_block,process_finish):
        self.process_running_frame.update_process(process_running)
        self.process_ready_frame.update_process(process_ready)
        self.process_block_frame.update_process(process_block)
        self.process_finish_frame.update_process(process_finish)

    #        self.process_available_frame.update_process(process_available)    