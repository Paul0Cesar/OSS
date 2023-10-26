import customtkinter
from src.widgets.button_frame import ButtonFrame
from src.widgets.animation_frame import AnimationFrame
from src.widgets.process_frame import ProcessFrame
from src.widgets.cpu_status_frame import CpuStatusFrame
from src.widgets.memory_frame import MemoryFrame
from src.widgets.gantt import Gantt
import tkinter as tk
import random

from src.models.pcb import PCB
from src.models.page import Page
from src.core.kernel import Kernel
from src.models.historic_element import HistoricElement

from typing import List
import queue
import threading


class Simulation():

    def __init__(self, master, process_list):

        self.master = master
        self.kernel_thread = None
        self.is_running = False
        self.process_list = process_list

        self.process_running = []
        self.process_ready = []
        self.process_block = []
        self.process_finish = []
        self.process_available = []
        self.ram_memory = []
        self.historic_queue = queue.Queue()
        self.kernel = Kernel(self.historic_queue, 5)

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
            master=master, start_process=self.start_new_process, width=300, fg_color="white")
        self.process_frame.grid(
            row=2, column=0, padx=10, pady=10, sticky="nsew")

        self.gantt = Gantt(master=master, fg_color="red")
        self.gantt.grid(row=3, column=0, columnspan=2,
                        padx=10, pady=10, sticky="nsew")

        self.primary_memory_frame = MemoryFrame(
            master=master, height=50, lines=1, columns=6, fg_color="white", border_width=1, corner_radius=12)
        self.primary_memory_frame.grid(
            row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")
        # self.primary_memory_frame.mock_elements()

        self.cpu_status_frame = CpuStatusFrame(
            master=master, width=10, height=10, fg_color="white")
        self.cpu_status_frame.grid(
            row=2, column=1, padx=10, pady=10, sticky="nsew")

        self.memory_disc_frame = MemoryFrame(
            master=master, lines=3, columns=6, fg_color="white", border_width=1, corner_radius=12)
        self.memory_disc_frame.grid(
            row=0, column=2, padx=10, rowspan=4, pady=10, sticky="nsew")
        # self.memory_disc_frame.mock_elements()

        master.after(500, self.update_view_callback)

    def toggle_action_buttons_visibility(self):
        self.button_frame.toggle_action_buttons_visibility(self.is_running)

    def start_new_process(self, process):
        new_process = PCB(
            creation_time=random.randint(1, 100),
            PID=random.randint(1, 100),
            icon=process.icon,
            name=process.name,
            total_time=process.total_time,
            pages=process.pages)
        
        self.process_available.remove(process)
        self.process_frame.set_available_process(self.process_available)
        self.kernel.add_PCB(new_process)
        print("NOVO")

    def start(self):
        print("START!")
        self.kernel_thread = None
        self.kernel.clear()
        for i in self.process_list:
            if (i.creation_time != -1):
                self.kernel.add_PCB(i)
            else:
                self.process_available.append(i)

        self.process_frame.set_available_process(self.process_available)

        self.memory_disc_frame.setElements(self.kernel.get_all_memory_ram())

        self.kernel_thread = threading.Thread(target=self.kernel.execute)
        self.is_running = True
        self.toggle_action_buttons_visibility()
        self.kernel_thread.start()

    def stop(self):
        print("STOP!")
        self.kernel_thread.join()
        self.is_running = False
        self.toggle_action_buttons_visibility()
        self.kernel_thread = None

    def update_view(self):
        if not self.is_running:
            return
        try:
            payload = self.historic_queue.get(block=False)
        except queue.Empty:
            if self.is_running:
                self.stop()
            print("Execution queue empty!")
        else:
            self.process_ready = self.kernel.execution_list

            if (payload.statistic):
                self.cpu_status_frame.setStatus(
                    payload.statistic.ram_use,
                    payload.statistic.swap_use,
                    payload.statistic.pagination_rate)
                # print(payload.statistic)

            if (payload.swap_in and payload.swap_out):
                self.ram_memory[self.ram_memory.index(
                    payload.swap_out)] = payload.swap_in
            elif (payload.swap_in):
                self.ram_memory.append(payload.swap_in)

            self.primary_memory_frame.setElements(self.ram_memory)

            if (payload.process_in_execution):
                self.gantt.plot_execution_bar(payload.process_in_execution)
                if payload.process_in_execution in self.process_ready:
                    self.process_ready.remove(payload.process_in_execution)

                if payload.process_in_execution not in self.process_running:
                    self.process_running.append(
                        payload.process_in_execution)

            if (payload.process_to_await):
                self.gantt.add_process(payload.process_to_await)
                if (payload.page_fault):
                    self.gantt.plot_stop_bar(payload.process_to_await)
                if (payload.process_to_await in self.process_running):
                    self.process_running.remove(payload.process_to_await)
                self.process_block.append(payload.process_to_await)

            if (payload.process_to_finish):
                if (payload.process_to_finish in self.process_running):
                    self.process_running.remove(payload.process_to_finish)
                if (payload.process_to_finish not in self.process_finish):
                    self.process_finish.append(payload.process_to_finish)

            if (payload.process_to_execution):
                self.gantt.add_process(payload.process_to_execution)
                if (payload.process_to_execution in self.process_block):
                    self.process_block.remove(payload.process_to_execution)
                if (payload.process_to_execution not in self.process_ready):
                    self.process_ready.append(payload.process_to_execution)

            self.process_frame.update_process(
                self.process_running,
                self.process_ready,
                self.process_block,
                self.process_finish)

    def update_view_callback(self):
        self.update_view()
        self.master.after(1000, self.update_view_callback)
