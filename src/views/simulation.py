import customtkinter
from src.widgets.button_frame import ButtonFrame
from src.widgets.animation_frame import AnimationFrame
from src.widgets.process_frame import ProcessFrame
from src.widgets.memory_frame import MemoryFrame
import tkinter as tk


class Simulation():
    def __init__(self, master):

        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=1)
        master.grid_columnconfigure(2, weight=1)

        self.button_frame = ButtonFrame(master=master, fg_color="white")
        self.button_frame.grid(row=0, column=0, sticky=tk.N)

        self.animation_frame = AnimationFrame(master=master, fg_color="red")
        self.animation_frame.grid(
            row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.process_frame = ProcessFrame(
            master=master, width=300, fg_color="white")
        self.process_frame.grid(
            row=2, column=0, padx=10, pady=10, sticky="nsew")

        self.primary_memory_frame = MemoryFrame(
            master=master,height=50, fg_color="white", border_width=1, corner_radius=12)
        self.primary_memory_frame.grid(
            row=0, column=1,rowspan=2, padx=10,pady=10, sticky="nsew")

        self.memory_disc_frame = MemoryFrame(
            master=master, lines=16, fg_color="white", border_width=1, corner_radius=12)
        self.memory_disc_frame.grid(
            row=0, column=2, padx=10, rowspan=4, pady=10, sticky="nsew")
