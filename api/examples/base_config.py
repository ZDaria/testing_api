from testing_api.config.config import Config

class BaseConfig:

    def __init__(self):
        self.url = f"{Config.api_url}"
