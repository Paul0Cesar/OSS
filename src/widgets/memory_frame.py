import customtkinter


class MemoryFrame(customtkinter.CTkFrame):
    def __init__(self, master, lines=11, columns=8, **kwargs):
        super().__init__(master, **kwargs)
        self.lines = lines
        self.columns = columns
        for i in range(self.lines):
            self.grid_rowconfigure(i, weight=1)
            for j in range(self.columns):
                self.grid_columnconfigure(j, weight=1)

    def create_item(self, text, row, colum):
        button = customtkinter.CTkButton(
            master=self, bg_color="transparent", border_color="black", border_width=1, fg_color="transparent", text=text, width=20, height=20)
        button.grid(row=row, column=colum, padx=5, pady=3)

    def mock_elements(self):
        for i in range(self.lines):
            for j in range(self.columns):
                self.create_item("AA", i, j)
