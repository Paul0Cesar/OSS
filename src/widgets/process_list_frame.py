import customtkinter
from PIL import Image


class ProcessListFrame(customtkinter.CTkFrame):
    def __init__(self, master, orientation="horizontal", **kwargs):
        super().__init__(master, **kwargs)
        self.orientation = orientation
        self.last_process_list=None

    def create_item(self, icon_url, index):
        icon = customtkinter.CTkImage(
            light_image=Image.open(icon_url), size=(15, 15))
        button = customtkinter.CTkButton(
            master=self, text="", bg_color="transparent", fg_color="transparent", image=icon, width=20, height=20)
        if (self.orientation == "horizontal"):
            button.grid(row=0, column=index, padx=5, pady=5)
        else:
            button.grid(row=index, column=0, padx=5, pady=5)

    def update_process(self,itens):
        if(itens==self.last_process_list):
            return
        self.last_process_list=itens
        index = 0
        for item in itens:
            index = index+1
            self.create_item(item.icon, index)

    def mock_elements(self):
        index = 0
        itens = ["src/resources/icons/chrome.png",
                 "src/resources/icons/terminal.png"]
        for item in itens:
            index = index+1
            self.create_item(item, index)
