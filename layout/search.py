import os
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QFileDialog
from PyQt6.QtCore import QDir
from widgets import CoverImage, MangaSearch, Button, CheckButton
from functions import Manga, Config


class SearchLayout(QWidget):

  def __init__(self, window):
    super().__init__()

    config = Config()

    self.window = window
    self.config = Config()
    self.save_as_pdf_state = False

    self.mange = Manga(window, self.enabled_button)

    self.cover_image = CoverImage()
    cover_image_widget = self.cover_image.init_ui()

    self.manga_search = MangaSearch()
    self.manga_search = self.manga_search.init_ui()
    self.search_button = Button(config['WIDGET']['BUTTON']['SEARCH'])
    self.search_button = self.search_button.init_ui()
    self.download_button = Button(config['WIDGET']['BUTTON']['DOWNLOAD'])
    self.download_button = self.download_button.init_ui()
    self.save_as_pdf_button = CheckButton(config['WIDGET']['BUTTON']['PDF'])
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
    self.save_as_pdf_button.setEnabled(enabled)

  def save_as_pdf_toggled(self):
    self.save_as_pdf_state = self.save_as_pdf_button.isChecked()

  def search(self):
    self.mange.init(self.manga_search.text())

    if self.mange.check():
      cover_url = self.mange.get_cover()

      self.cover_image.set_cover(cover_url)
      self.window.setWindowTitle(self.config['MESSAGE']['SEARCH']['SUCCESS'])
    else:
      self.cover_image.reset_cover()
      self.window.setWindowTitle(self.config['MESSAGE']['SEARCH']['ERROR'])

    self.enabled_button(True)

  def download(self):
    download_folder = os.path.join(QDir.homePath(), 'Downloads')
    download_path = QFileDialog.getExistingDirectory(
        self, self.config['WIDGET']['FILEDIALOG'], download_folder)

    if download_path:
      self.mange.download(download_path, self.save_as_pdf_state)
