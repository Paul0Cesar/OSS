import customtkinter
from PIL import Image


class ProcessListFrame(customtkinter.CTkFrame):
    def __init__(self, master, start_process=None, orientation="horizontal", **kwargs):
        super().__init__(master, **kwargs)
        self.orientation = orientation
        self.start_process = start_process
        self.last_process_list = None
        self.processes = []

    def create_item(self, process, index):
        icon = customtkinter.CTkImage(
            light_image=Image.open(process.icon), size=(15, 15))
        button = customtkinter.CTkButton(
            master=self, text="", bg_color="transparent", fg_color="transparent", image=icon, width=20, height=20)
        if self.start_process:
            button = customtkinter.CTkButton(
                master=self, text="", bg_color="transparent", fg_color="transparent", image=icon, width=20, height=20, command=lambda: self.start_process(process))
        if (self.orientation == "horizontal"):
            button.grid(row=0, column=index, padx=5, pady=5)
        else:
            button.grid(row=index, column=0, padx=5, pady=5)
        return button

    def update_process(self, itens):
        for view in self.processes:
            view.destroy()

        self.last_process_list = itens
        index = 0
        for item in itens:
            index = index+1
            bt = self.create_item(item, index)
            self.processes.append(bt)

    def mock_elements(self):
        index = 0
        itens = ["src/resources/icons/chrome.png",
                 "src/resources/icons/terminal.png"]
        for item in itens:
            index = index+1
            self.create_item(item, index)
