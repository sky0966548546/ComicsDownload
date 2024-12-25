import configparser


class Config:

  def __init__(self, config_name):
    self.config_name = config_name

  def load(self):
    config_parser = configparser.ConfigParser()
    config_parser.read(self.config_name)

    return config_parser
