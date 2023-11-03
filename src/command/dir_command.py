from src.handler.config_handler import ConfigHandler

import os 

class DirCommand:
    def __init__(self, config: ConfigHandler):
        self.config = config 

    #this function create path doesn't exist
    def create_path(self):
        path_data = self.config.get_path_data()
        path_cut = self.config.get_path_cut()
        path_test =  self.config.get_path_test()
        path_compare = self.config.get_path_comp()

        if(os.path.isdir(path_data) == False):
            clip = os.path.join('shared', 'data')
            os.makedirs(clip)

        if(os.path.isdir(path_cut) == False):
            clip = os.path.join(path_data, 'clip')
            os.makedirs(clip)
        
        if(os.path.isdir(path_test) == False):
            clip = os.path.join(path_data, 'test')
            os.makedirs(clip)

        if(os.path.isdir(path_compare) == False):
            clip = os.path.join(path_test, 'compare')
            os.makedirs(clip)
        


        

        