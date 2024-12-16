from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import Qt
from functions import Config


class Button(QPushButton):

  def __init__(self, main_config, name):
    super().__init__()

    self.main_config = main_config

    config = Config(self.main_config['Paths']['config'])

    self.widget_config = config.load_config('widget_config')
    self.name = name

  def init_ui(self):
    self.setText(self.widget_config['Button'][self.name])
    self.setFixedHeight(40)
    self.setCursor(Qt.CursorShape.PointingHandCursor)
    self.setStyleSheet('''
      QPushButton {
        background-color: #333333;
        color: #FFFFFF;
        border: 2px solid #555555;
        padding: 10px 20px;
        font-size: 14px;
        border-radius: 4px;
      }
      QPushButton:hover {
        background-color: #444444;
        color: #DDDDDD;
        border-color: #777777;
      }
    ''')

    return self
