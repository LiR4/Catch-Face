from src.handler.config_handler import ConfigHandler

import cv2
import numpy as np
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from deepface import DeepFace

class VideoCommand:
    def __init__(self, config:ConfigHandler):

        self.config = config
        self.results = []
        self.last_time = []
        self.time_start = 0.0
        self.time_end = 0.0
        self.count = 0


    def cut(self,video_file, time_start, time_end, count, second):
        ffmpeg_extract_subclip(video_file, time_start, time_end+second, targetname=self.config.get_path_cut()+f'\cut{count}.mp4')


    def get_faces_on_video(self, video_file, seconds=3):

        video = cv2.VideoCapture(video_file)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

        while True:
            sucess, img = video.read()
            faces = face_cascade.detectMultiScale(img, 1.3, 4)
        
            if(type(faces).__module__ == np.__name__):
                self.time_start = (video.get(cv2.CAP_PROP_POS_MSEC))/1000
                self.last_time.append(self.time_start)
            
            if(type(faces).__module__ != np.__name__):
                self.time_end = (video.get(cv2.CAP_PROP_POS_MSEC))/1000
            
            if(self.time_start != 0.0 and self.time_end != 0.0): # cut section
                if(self.last_time[self.count]+1 < self.time_start):
                    self.cut(video_file, self.time_start, self.time_end, self.count, seconds)
                    print(f"time start: {self.time_start}, time end: {self.time_end+seconds}")
                    self.count += 1

                self.time_start = 0.0
                self.time_end = 0.0

        
            # cv2.imshow("teste",img)
            if sucess != True:
                break