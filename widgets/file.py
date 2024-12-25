import os
import importlib.resources as resources
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QMessageBox, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QIcon, QFont
from assets import images


class LockFile:

  def __init__(self, app, lock_file_path):
    self.app = app
    self.title = '漫画ダウンローダー'
    self.lock_file_path = lock_file_path

  def create(self):
    self.app.setApplicationName(self.title)

    if os.path.exists(self.lock_file_path):
      message_box = QMessageBox()

      with resources.as_file(resources.files(images) /
                             'icon.ico') as icon_path:
        message_box.setWindowTitle(self.title)
        message_box.setWindowIcon(QIcon(str(icon_path)))
        message_box.setStandardButtons(QMessageBox.StandardButton.Ok)

      label = QLabel('アプリケーションは既に実行中です。')
      font = QFont()
      font.setPointSize(10)
      label.setFont(font)
      label.setAlignment(Qt.AlignmentFlag.AlignCenter)

      layout = QVBoxLayout()
      layout.addWidget(label)
      layout_widget = QWidget()
      layout_widget.setLayout(layout)

      message_box.layout().addWidget(layout_widget, 0, 0, 1,
                                     message_box.layout().columnCount())
      message_box.exec()

      raise SystemExit(1)
    else:
      with open(self.lock_file_path, 'w') as lock_file:
        lock_file.write(str(os.getpid()))

  @staticmethod
  def remove(lock_file_path):
    if os.path.exists(lock_file_path):
      os.remove(lock_file_path)
