from src.command.view_command import AppCommand

import customtkinter
from dataclasses import dataclass

@dataclass
class App:

    def __init__(self, view_command:AppCommand):
        self.command = view_command

    def home(self):

        customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

        app = customtkinter.CTk()  # create CTk window like you do with the Tk window
        app.geometry("400x240")

        # Use CTkButton instead of tkinter Button
        button1 = customtkinter.CTkButton(master=app, text="File", command=self.command.video_file)
        button2= customtkinter.CTkButton(master=app, text="Directory", command=self.command.compare_dir)
        button1.place(relx=0.25, rely=0.5, anchor=customtkinter.CENTER)
        button2.place(relx=0.7, rely=0.5, anchor=customtkinter.CENTER)

        app.mainloop()