from dataclasses import dataclass
import configparser

@dataclass
class ConfigHandler:
    config = configparser.ConfigParser()
    config.read(r"shared\config.ini", encoding="utf-8-sig")

    def get_path_video(self) -> str:
        return self.config.get("path", "video")