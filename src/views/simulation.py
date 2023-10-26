import customtkinter
from src.widgets.button_frame import ButtonFrame
from src.widgets.animation_frame import AnimationFrame
from src.widgets.process_frame import ProcessFrame
from src.widgets.cpu_status_frame import CpuStatusFrame
from src.widgets.memory_frame import MemoryFrame
from src.widgets.gantt import Gantt
import tkinter as tk

from src.models.pcb import PCB
from src.models.page import Page
from src.core.kernel import Kernel
from src.models.historic_element import HistoricElement

from typing import List
import queue
import threading


class Simulation():

    def __init__(self, master,process_list):

        self.master = master
        self.kernel_thread = None
        self.historic_queue = queue.Queue()
        self.kernel = Kernel(self.historic_queue, 5)


        # self.kernel.add_PCB(self.pc1)
        # self.kernel.add_PCB(self.pc2)
        # self.kernel.add_PCB(self.pc3)

        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=1)
        master.grid_columnconfigure(2, weight=1)

        self.button_frame = ButtonFrame(
            master=master, start=self.start, stop=self.stop, fg_color="white")
        self.button_frame.grid(row=0, column=0, sticky=tk.N)

        # self.animation_frame = AnimationFrame(master=master, fg_color="red")
        # self.animation_frame.grid(
        #     row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.process_frame = ProcessFrame(
            master=master, width=300, fg_color="white")
        self.process_frame.grid(
            row=2, column=0, padx=10, pady=10, sticky="nsew")

        self.gantt = Gantt(master=master, fg_color="red")
        self.gantt.grid(row=3, column=0, columnspan=2,
                        padx=10, pady=10, sticky="nsew")

        # self.gantt.add_process(self.pc1)
        # self.gantt.add_process(self.pc2)
        # self.gantt.add_process(self.pc3)
        # self.gantt.update_view()

        # i=0
        # while(i<10):
        #     self.gantt.plot_execution_bar(pc1)
        #     i=i+1

        self.primary_memory_frame = MemoryFrame(
            master=master, height=50, fg_color="white", border_width=1, corner_radius=12)
        self.primary_memory_frame.grid(
            row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")
        # self.primary_memory_frame.mock_elements()

        self.cpu_status_frame = CpuStatusFrame(
            master=master, width=10, height=10, fg_color="white")
        self.cpu_status_frame.grid(
            row=2, column=1, padx=10, pady=10, sticky="nsew")

        self.memory_disc_frame = MemoryFrame(
            master=master, lines=16, fg_color="white", border_width=1, corner_radius=12)
        self.memory_disc_frame.grid(
            row=0, column=2, padx=10, rowspan=4, pady=10, sticky="nsew")
        # self.memory_disc_frame.mock_elements()

        master.after(500, self.update_view)

    def start(self):
        print("START!")
        self.kernel_thread = None
        self.kernel_thread = threading.Thread(target=self.kernel.execute)
        self.kernel_thread.start()

    def stop(self):
        print("STOP!")
        self.kernel_thread.join()
        self.kernel_thread = None

    def update_view(self):
        # process_running = [self.pc1]
        # process_ready = [self.pc2]
        # process_block = [self.pc3]
        # process_finish = []

        # self.process_frame.update_process(
        #     process_running, process_ready, process_block, process_finish)
        # self.historic
        # while True:
        #     try:
        #         record = self.historic_queue.get(block=False)
        #     except queue.Empty:
        #         break
        #     else:
        #         print(record)
        #         print("update_view!!")
        #         # self.display(record)

        self.master.after(500, self.update_view)
