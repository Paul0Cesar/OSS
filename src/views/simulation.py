import customtkinter
from src.widgets.button_frame import ButtonFrame
from src.widgets.animation_frame import AnimationFrame
from src.widgets.process_frame import ProcessFrame
import tkinter as tk


class Simulation():
    def __init__(self, master):
        self.button_frame = ButtonFrame(master=master, fg_color="white")
        self.button_frame.grid(row=0, column=0, sticky=tk.N)

        self.animation_frame = AnimationFrame(master=master, fg_color="red")
        self.animation_frame.grid(
            row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.process_frame = ProcessFrame(
            master=master, width=300, fg_color="white")
        self.process_frame.grid(
            row=2, column=0, padx=10, pady=10, sticky="nsew")
