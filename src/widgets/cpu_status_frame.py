import customtkinter
from src.utils.constants import *


class CpuStatusFrame(customtkinter.CTkFrame):
    def __init__(self, master,**kwargs):
        super().__init__(master, **kwargs)

        self.ram_label = customtkinter.CTkLabel(self,text=RAM)
        self.ram_label.pack()
        self.ram_status = customtkinter.CTkProgressBar(self)
        self.ram_status.pack()

        self.swap_label = customtkinter.CTkLabel(self,text=SWAP)
        self.swap_label.pack()
        self.swap_status = customtkinter.CTkProgressBar(self)
        self.swap_status.pack()

        self.pagination_label = customtkinter.CTkLabel(self,text=PAGINATION)
        self.pagination_label.pack()
        self.pagination_status = customtkinter.CTkProgressBar(self)
        self.pagination_status.pack()

    
    def setStatus(self,ram,swap,pagination):
        self.ram_status.set(ram)
        self.swap_status.set(swap)
        self.pagination_status.set(pagination)

    def mock_values(self):
        self.ram_status.set(0.5)
        self.swap_status.set(0.5)
        self.pagination_status.set(0.5)