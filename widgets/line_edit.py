from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtGui import QIntValidator


class MangaSearch(QLineEdit):

  def __init__(self):
    super().__init__()

  def init_ui(self):
    self.setFixedHeight(40)
    self.setValidator(QIntValidator())
    self.setCursor(Qt.CursorShape.CustomCursor)
    self.setStyleSheet('''
      background-color: #333333;
      color: #FFFFFF;
      padding: 10px 20px;
      font-size: 14px;
      border-radius: 4px;
    ''')

    return self
