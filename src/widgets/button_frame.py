import customtkinter


class ButtonFrame(customtkinter.CTkFrame):
    def __init__(self, master,start,stop, **kwargs):
        super().__init__(master, **kwargs)

        self.start_button = customtkinter.CTkButton(
            self, text="Start", command=start)
        self.start_button.grid(row=0, column=0, padx=20, pady=10)
        self.stop_button = customtkinter.CTkButton(
            self, text="Stop", command=stop)
        self.stop_button.grid(row=0, column=1, padx=20, pady=10)
