import customtkinter
from src.utils.constants import *


class CpuStatusFrame(customtkinter.CTkFrame):
    def __init__(self, master,**kwargs):
        super().__init__(master, **kwargs)

        self.ram_label = customtkinter.CTkLabel(self,text=RAM)
        self.ram_label.grid(row=0, column=0, padx=20)
        self.ram_status = customtkinter.CTkProgressBar(self)
        self.ram_status.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")

        self.swap_label = customtkinter.CTkLabel(self,text=SWAP)
        self.swap_label.grid(row=2, column=0, padx=20)
        self.swap_status = customtkinter.CTkProgressBar(self)
        self.swap_status.grid(row=3, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")

        self.pagination_label = customtkinter.CTkLabel(self,text=PAGINATION)
        self.pagination_label.grid(row=4, column=0, padx=20)
        self.pagination_status = customtkinter.CTkProgressBar(self)
        self.pagination_status.grid(row=5, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")



    def mock_values(self):
        self.ram_status=0.5
        self.swap_status=0.5
        self.pagination_status=0.5