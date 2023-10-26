import customtkinter
from tkinter import *


class MemoryFrame(customtkinter.CTkFrame):
    def __init__(self, master, lines=11, columns=8, **kwargs):
        super().__init__(master, **kwargs)
        self.lines = lines
        self.columns = columns
        self.elements_view=[]
        for i in range(self.lines):
            self.grid_rowconfigure(i, weight=1)
            for j in range(self.columns):
                self.grid_columnconfigure(j, weight=1)

    def create_item(self, text, row, colum):
        # item = customtkinter.CTkButton(
        #     master=self, border_color="black", border_width=1, text=text, width=20, height=20)
        item=Label(self,text=text)
        item.grid(row=row, column=colum, padx=5, pady=3)
        return item

    def setElements(self,elements):

        for view in self.elements_view:
            view.destroy()

        size=len(elements)
        if(size==0):
            return  
        index=0
        for i in range(self.lines):
            if index>=size:
                    break
            for j in range(self.columns):
                bt=self.create_item(elements[index].name, i, j)
                self.elements_view.append(bt)
                index=index+1
                if index>=size:
                    break

    def mock_elements(self):
        for i in range(self.lines):
            for j in range(self.columns):
                self.create_item("AA", i, j)
