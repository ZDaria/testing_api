from pathlib import Path
import os
import configparser


class Config:
    """Абстрактный класс"""
    api_url: str
    debug: bool = False
    stand: str
    log_level = "INFO"
    timeout: int = 20
    root_dir = os.path.dirname(os.path.abspath(__file__))
    logs_dir: Path = os.path.join(root_dir, "logs_dir")
    temp_dir: Path = os.path.join(root_dir, "temp_dir")
    jenkins: bool = False
    allure: Path

    @staticmethod
    def get_config(config_name: str) -> dict:
        config_path = os.path.join(Config.root_dir, "/configs", config_name)
        config = configparser.ConfigParser()
        config.read(config_path, encoding="UTF-8")

        return config

    @staticmethod
    def get_moex_config():
        return Config.get_config("moex.ini")

    @staticmethod
    def get_example_orders_config():
        return Config.get_config("example_orders.ini")
