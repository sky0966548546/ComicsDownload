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
        background-color: #3A3A3A;
        color: #FFFFFF;
        border: 2px solid #555555;
        padding: 10px 20px;
        font-size: 14px;
        border-radius: 6px;
      }

      QPushButton:hover {
        background-color: #505050;
        color: #F0F0F0;
        border-color: #888888;
      }

      QPushButton:pressed {
        background-color: #2A2A2A;
        border-color: #666666;
        color: #E0E0E0;
      }

      QPushButton:disabled {
        background-color: #4A4A4A;
        color: #B0B0B0;
        border-color: #666666;
      }
    ''')

    return self
