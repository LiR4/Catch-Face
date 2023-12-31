from src.command.view_command import AppCommand
from src.command.video_command import VideoCommand

import customtkinter
from dataclasses import dataclass

@dataclass
class App:

    def __init__(self, view_command:AppCommand, video:VideoCommand):
        self.command = view_command
        self.video = video

    def home(self):

        customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

        app = customtkinter.CTk()  # create CTk window like you do with the Tk window
        app.geometry("400x240")

        def start():
            self.video.get_faces_on_video()

        def move():
            self.video.move_clips()
        

        # Use CTkButton instead of tkinter Button
        button1 = customtkinter.CTkButton(master=app, text="Start", command=start)
        button1.place(relx=0.25, rely=0.4, anchor=customtkinter.CENTER)
        button2 = customtkinter.CTkButton(master=app, text="Move clips", command=move)
        button2.place(relx=0.75, rely=0.4, anchor=customtkinter.CENTER)

        app.mainloop()
