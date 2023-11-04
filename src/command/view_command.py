import customtkinter

class AppCommand:
    def __init__(self):
        pass

    def video_file(self):
        filename = customtkinter.filedialog.askopenfile()
        print(filename.name)

    def compare_dir(self):
        filename = customtkinter.filedialog.askdirectory()
        print(filename)