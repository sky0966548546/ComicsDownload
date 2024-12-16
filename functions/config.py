import os
import configparser


class Config:

  def __init__(self, path):
    self.path = path

  def load_config(self, name):
    config_path = os.path.join(self.path, f'{name}.ini')

    config = configparser.ConfigParser()
    config.read(config_path)

    return config
