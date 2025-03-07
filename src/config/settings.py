from os import getenv
from dotenv import load_dotenv
from pathlib import Path

from model.config_env import ConfigEnv

class Settings:

    def __init__(self, config_env: ConfigEnv):
        self.load_settings(config_env)

    def load_settings(self, config_env: ConfigEnv):
        env_filename = f"{config_env.value}.env"
        env_path = Path(__file__).parent.parent / "env" / env_filename
        load_dotenv(dotenv_path=env_path.absolute())

    def get_opensearch_url(self) -> str:
        return getenv("OPENSEARCH_URL", "")
    
    def get_opensearch_usr(self) -> str:
        return getenv("OPENSEARCH_USR", "")
    
    def get_opensearch_psw(self) -> str:
        return getenv("OPENSEARCH_PSW", "")