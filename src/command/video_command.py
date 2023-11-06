from src.handler.config_handler import ConfigHandler
from src.command.view_command import AppCommand

import cv2
import numpy as np
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from deepface import DeepFace
import os

class VideoCommand:
    def __init__(self, config:ConfigHandler, app:AppCommand):

        self.config = config
        self.results = []
        self.last_time = []
        self.results = []
        self.time_start = 0.0
        self.time_end = 0.0
        self.count = 0
        self.path_cut = config.get_path_cut()
        self.path_compare = app.compare_dir()
        self.path_video = app.video_file()


    def cut(self,video_file, time_start, time_end, count, second):
        ffmpeg_extract_subclip(video_file, time_start, time_end+second, targetname=self.config.get_path_cut()+f'\cut{count}.mp4')


    def get_faces_on_video(self, seconds=3):

        video = cv2.VideoCapture(self.path_video)
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
                    self.cut(self.path_video, self.time_start, self.time_end, self.count, seconds)
                    print(f"time start: {self.time_start}, time end: {self.time_end+seconds}")
                    self.count += 1

                self.time_start = 0.0
                self.time_end = 0.0

        
            # cv2.imshow("teste",img)
            if sucess != True:
                break

        self.clips_have_face()

    def catch_face(self, file, compare):
        video = cv2.VideoCapture(file)
        if(video.isOpened):
            while True:
                state, frames = video.read()
                if(state):
                    cv2.imwrite('./shared/data/test/teste.jpg', frames)
                    dfs = DeepFace.find(img_path = './shared/data/test/teste.jpg', db_path = compare, enforce_detection=False)
                    if(len(dfs[0])!=0):
                        self.results.append(file)
                        break
                else:
                    break

    def clips_have_face(self):
        for file in os.listdir(self.path_cut):
            print("--------\n",self.path_cut+'\\'+file,"\n--------")
            self.catch_face(self.path_cut+'\\'+file,self.path_compare)

        print(self.results)