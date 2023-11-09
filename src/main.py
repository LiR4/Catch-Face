from src.handler.config_handler import ConfigHandler
from src.command.dir_command import DirCommand
from src.command.video_command import VideoCommand
from src.command.view_command import AppCommand
from src.view.app import App


config = ConfigHandler()

directory = DirCommand(config)

app_command = AppCommand()

video = VideoCommand(config, app_command)

directory.create_path()

view = App(app_command, video)

view.home()

#you need to chage a foto in directory shared\data\test\compare
# print(video.clips_have_face())


