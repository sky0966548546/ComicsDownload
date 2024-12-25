import os
import atexit
import importlib.resources as resources
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QFrame, QWidget
from PyQt6.QtGui import QIcon
from widgets import LockFile
from layout import SearchLayout
from assets import images


class MainWindow(QMainWindow):

  def __init__(self):
    super().__init__()

    title = '漫画ダウンローダー'
    width = 400
    height = 500

    with resources.as_file(resources.files(images) / 'icon.ico') as icon_path:
      self.setWindowTitle(title)
      self.setWindowIcon(QIcon(str(icon_path)))
      self.setFixedSize(width, height)

    search_layout = SearchLayout(self)

    line = QFrame()
    line.setFrameShape(QFrame.Shape.VLine)
    line.setStyleSheet('color: gray;')

    main_widget = QWidget()
    main_layout = QGridLayout()

    main_widget.setLayout(main_layout)
    self.setCentralWidget(main_widget)

    main_layout.addWidget(search_layout)

  def closeEvent(self, event):
    lock_file_path = os.path.join(os.getcwd(), 'app.lock')
    LockFile.remove(lock_file_path)
    event.accept()


if __name__ == '__main__':
  app = QApplication([])
  app.setStyle('Fusion')

  lock_file_path = os.path.join(os.getcwd(), 'app.lock')

  lock_file = LockFile(app, lock_file_path)
  lock_file.create()
  atexit.register(lambda: LockFile.remove(lock_file_path))

  window = MainWindow()

  window.show()
  app.exec()
