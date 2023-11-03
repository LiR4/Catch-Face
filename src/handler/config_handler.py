from dataclasses import dataclass
import configparser

@dataclass
class ConfigHandler:
    config = configparser.ConfigParser()
    config.read(r"shared\config.ini", encoding="utf-8-sig")

    def get_path_data(self) -> str:
        return self.config.get("path", "data")
    
    def get_path_cut(self) -> str: 
        return self.config.get("path", "cut")
    
    def get_path_test(self) -> str: 
        return self.config.get("path", "test")
    
    def get_path_comp(self) -> str: 
        return self.config.get("path", "compare")