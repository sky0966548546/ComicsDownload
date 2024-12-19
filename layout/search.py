import os
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QFileDialog
from PyQt6.QtCore import QDir
from widgets import CoverImage, MangaSearch, Button, CheckButton
from functions import Manga


class SearchLayout(QWidget):

  def __init__(self, main_config, window):
    super().__init__()

    self.main_config = main_config
    self.window = window
    self.title = self.main_config['General']['title']
    self.save_as_pdf_state = False

    self.mange = Manga(self.main_config, window, self.enabled_button)

    self.cover_image = CoverImage(self.main_config)
    cover_image_widget = self.cover_image.init_ui()

    self.manga_search = MangaSearch()
    self.manga_search = self.manga_search.init_ui()
    self.search_button = Button(self.main_config, 'search')
    self.search_button = self.search_button.init_ui()
    self.download_button = Button(self.main_config, 'download')
    self.download_button = self.download_button.init_ui()
    self.save_as_pdf_button = CheckButton(self.main_config, 'pdf')
    self.save_as_pdf_button = self.save_as_pdf_button.init_ui()

    self.download_button.setEnabled(False)
    self.save_as_pdf_button.setCheckable(True)

    search_button_layout = QHBoxLayout()
    search_button_layout.addWidget(self.search_button)
    search_button_layout.addWidget(self.download_button)
    search_button_layout.addWidget(self.save_as_pdf_button)

    layout = QVBoxLayout(self)
    layout.addLayout(cover_image_widget)
    layout.addSpacing(10)
    layout.addWidget(self.manga_search)
    layout.setSpacing(10)
    layout.addLayout(search_button_layout)
    layout.setSpacing(10)
    layout.addStretch()

    self.setLayout(layout)

    self.search_button.clicked.connect(lambda: self.search())
    self.download_button.clicked.connect(lambda: self.download())
    self.save_as_pdf_button.toggled.connect(lambda: self.save_as_pdf_toggled())

  def enabled_button(self, enabled):
    self.search_button.setEnabled(enabled)
    self.download_button.setEnabled(enabled)

  def save_as_pdf_toggled(self):
    self.save_as_pdf_state = self.save_as_pdf_button.isChecked()

  def search(self):
    self.mange.init(self.manga_search.text())

    if self.mange.check():
      cover_url = self.mange.get_cover()

      self.cover_image.set_cover(cover_url)
      self.window.setWindowTitle(f'{self.title} | 接続成功')
    else:
      self.cover_image.reset_cover()
      self.window.setWindowTitle(f'{self.title} | 接続エラー、再入力してください')

    self.enabled_button(True)

  def download(self):
    download_folder = os.path.join(QDir.homePath(), 'Downloads')
    download_path = QFileDialog.getExistingDirectory(self, 'フォルダ選択',
                                                     download_folder)

    if download_path:
      self.mange.download(download_path, self.save_as_pdf_state)
