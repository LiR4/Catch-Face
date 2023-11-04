from src.handler.config_handler import ConfigHandler
from src.command.dir_command import DirCommand
from src.command.video_command import VideoCommand
from src.command.view_command import AppCommand
from src.view.app import App

app_command = AppCommand()

view = App(app_command)

view.home()

# video_file = r'shared\data\20231014_094039.mp4'

# config = ConfigHandler()

# directory = DirCommand(config)

# video = VideoCommand(config)

# directory.create_path()

# video.get_faces_on_video(video_file)

# #you need to chage a foto in directory shared\data\test\compare
# print(video.clips_have_face())


