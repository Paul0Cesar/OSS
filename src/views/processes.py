import customtkinter
from PIL import Image
import tkinter as tk


from src.models.pcb import PCB
import random
from src.models.page import Page


class Processes():

    def __init__(self, master, process_list):

        self.master = master
        icons = ["chrome.png", "terminal.png", "visual-studio-code.png",
                 "adobe-acrobat.png", "adobe-acrobat.png", "adobe-photoshop.png"]

        self.master.grid_columnconfigure(0, weight=0)
        self.master.grid_columnconfigure(1, weight=1)

        self.process_list = process_list
        self.all_process_buttons = []
        self.current_process = None

        self.name = tk.StringVar("")
        self.pages = tk.StringVar("")
        self.creation_time = tk.IntVar(0)
        self.execution_time = tk.IntVar()

        self.sidebar_frame = customtkinter.CTkFrame(
            master, fg_color="white", corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.scrollable_frame = customtkinter.CTkScrollableFrame(
            self.sidebar_frame, label_text="Processes")
        self.scrollable_frame.grid(row=0, column=0, padx=(
            20, 0), pady=(20, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame_switches = []

        self.entry_name = customtkinter.CTkEntry(
            master, textvariable=self.name, placeholder_text="Name:")
        self.entry_name.grid(row=0, column=1, padx=(
            20, 0), pady=(20, 0), sticky="nsew")

        self.entry_creation_time = customtkinter.CTkEntry(
            master, textvariable=self.creation_time, placeholder_text="Creation Time:")
        self.entry_creation_time.grid(
            row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        self.entry_execution_time = customtkinter.CTkEntry(
            master, textvariable=self.execution_time, placeholder_text="Creation Time:")
        self.entry_execution_time.grid(
            row=2, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        self.entry_pages = customtkinter.CTkEntry(
            master, textvariable=self.pages, placeholder_text="Pages(P1,P2,..):")
        self.entry_pages.grid(
            row=3, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.icon_menu = customtkinter.CTkOptionMenu(master, dynamic_resizing=False,
                                                     values=icons)
        self.icon_menu.grid(row=0, column=2, padx=20, pady=(20, 10))

        self.save_button = customtkinter.CTkButton(
            self.master, text="Save", command=self.save)
        self.save_button.grid(row=1, column=2, padx=20, pady=(20, 10))

        self.delele_button = customtkinter.CTkButton(
            master=self.master, text="Deletar", command=self.delete)
        # self.delele_button.grid(row=3, column=2, padx=20, pady=(20, 10))

        # self.delele_button = customtkinter.CTkButton(master=self,text="Deletar",command=self.delete)
        # self.confirm_button = customtkinter.CTkButton(master=self,text=button_label,command=self.save)
        self.update_process_list()

    def change_save_button_visibility(self, is_visibility):
        if is_visibility:
            self.save_button.grid(row=1, column=2, padx=20, pady=(20, 10))
        else:
            self.save_button.grid_forget()

    def change_delete_button_visibility(self, is_visibility):
        if is_visibility:
            self.delele_button.grid(row=2, column=2, padx=20, pady=(20, 10))
        else:
            self.delele_button.grid_forget()

    def delete(self):
        if (self.current_process is None):
            print("Don't have process selected!")
            return
        self.process_list.remove(self.current_process)

        self.name.set("")
        self.creation_time.set(0)
        self.execution_time.set(0)
        self.pages.set("")

        self.change_delete_button_visibility(False)
        self.update_process_list()

    def save(self):
        pages= list(map(lambda x: Page(x), self.pages.get().split(",")))
        if (self.current_process is None):
            process = PCB(creation_time=self.creation_time.get(),
                          PID=random.randint(1, 100),
                          icon="src/resources/icons/"+self.icon_menu.get(),
                          name=self.name.get(),
                          total_time=self.execution_time.get(),
                          pages=pages)
            self.process_list.append(process)
            self.update_process_list()
        else:
            self.current_process.name = self.name.get()
            self.current_process.creation_time = self.creation_time.get()
            self.current_process.total_time = self.execution_time.get()
            self.current_process.icon = "src/resources/icons/"+self.icon_menu.get()
            self.current_process.pages = pages
            self.change_delete_button_visibility(False)
            self.current_process =None

        self.name.set("")
        self.creation_time.set(0)
        self.execution_time.set(0)
        self.pages.set("")

    def update_process_list(self):
        index = 0
        for view in self.all_process_buttons:
            view.destroy()
        for process in self.process_list:
            item = self.create_process_view_element(index, process)
            self.all_process_buttons.append(item)
            index = index+1

    def process_selection(self, process):
        self.current_process = process
        self.name.set(process.name)
        self.creation_time.set(process.creation_time)
        self.execution_time.set(process.total_time)
        pages = list(map(lambda x: x.name, process.pages))

        self.pages.set(",".join(pages))

        self.icon_menu.set(process.icon.split("/")[3])
        self.change_delete_button_visibility(True)

    def create_process_view_element(self, index, process):
        icon = customtkinter.CTkImage(
            light_image=Image.open(process.icon), size=(15, 15))
        item = customtkinter.CTkButton(
            master=self.scrollable_frame, text=process.name, bg_color="transparent", fg_color="transparent", image=icon, width=20, height=20, command=lambda: self.process_selection(process))
        item.grid(row=index, column=0, padx=10, pady=(0, 20))
        return item
