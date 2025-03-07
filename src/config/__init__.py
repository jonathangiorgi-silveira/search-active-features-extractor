import sys

from model.config_env import ConfigEnv
from config.settings import Settings

config_env_param = sys.argv[1] if len(sys.argv) > 1 else ConfigEnv.QA.value
config_env = ConfigEnv.from_value(config_env_param)

settings = Settings(config_env=config_env)