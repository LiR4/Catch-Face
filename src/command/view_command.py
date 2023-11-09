import cv2
import customtkinter

class AppCommand:
    def __init__(self):
        pass

    def video_file(self):
        filename = customtkinter.filedialog.askopenfile()
        return filename.name

    def compare_dir(self):
        filename = customtkinter.filedialog.askdirectory()
        return filename
    
    def play_video(self, path):
        cap = cv2.VideoCapture(path)
        while True:
            ret, frame = cap.read()
            cv2.imshow('frame', frame)
            
            if ret != True:
                cap.release()
                cv2.destroyAllWindows
                break

