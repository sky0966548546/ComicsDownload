import sys
import os
import atexit
import configparser
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QFrame, QWidget
from PyQt6.QtGui import QIcon
from widgets import LockFile
from layout import SearchLayout

class MainWindow(QMainWindow):

  def __init__(self, config):
    super().__init__()

    self.setWindowTitle(config['General']['title'])
    self.setWindowIcon(QIcon(config['General']['icon']))
    self.setFixedSize(int(config['General']['width']),
                      int(config['General']['height']))

    search_layout = SearchLayout(config, self)

    line = QFrame()
    line.setFrameShape(QFrame.Shape.VLine)
    line.setStyleSheet('color: gray;')

    main_widget = QWidget()
    main_layout = QGridLayout()

    main_widget.setLayout(main_layout)
    self.setCentralWidget(main_widget)

    main_layout.addWidget(search_layout)


if __name__ == '__main__':
  app = QApplication(sys.argv)
  app.setStyle('Fusion')

  main_config_path = os.path.join(os.getcwd(), 'assets', 'config',
                                  'main_config.ini')
  lock_file_path = os.path.join(os.getcwd(), 'app.lock')

  config = configparser.ConfigParser()
  config.read(main_config_path)

  config['General']['icon'] = os.path.join(config['Paths']['images'],
                                           config['General']['icon'])

  lock_file = LockFile(app, config, lock_file_path)
  lock_file.create()
  atexit.register(lock_file.remove, lock_file_path)

  window = MainWindow(config)

  window.show()
  sys.exit(app.exec())
