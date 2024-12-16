from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QFileDialog
from widgets import CoverImage, MangaSearch, Button
from functions import Manga


class SearchLayout(QWidget):

  def __init__(self, main_config, window):
    super().__init__()

    self.main_config = main_config
    self.window = window
    self.mange = Manga(self.main_config)

    self.cover_image = CoverImage(self.main_config)
    cover_image_widget = self.cover_image.init_ui()

    self.manga_search = MangaSearch()
    self.manga_search = self.manga_search.init_ui()
    self.search_button = Button(self.main_config, 'search')
    self.search_button = self.search_button.init_ui()
    self.download_button = Button(self.main_config, 'download')
    self.download_button = self.download_button.init_ui()
    self.download_button.setEnabled(False)

    search_button_layout = QHBoxLayout()
    search_button_layout.addWidget(self.search_button)
    search_button_layout.addWidget(self.download_button)

    layout = QVBoxLayout(self)
    layout.addLayout(cover_image_widget)
    layout.addSpacing(20)
    layout.addWidget(self.manga_search)
    layout.setSpacing(10)
    layout.addLayout(search_button_layout)
    layout.setSpacing(10)
    layout.addStretch()

    self.setLayout(layout)

    self.search_button.clicked.connect(lambda: self.search())
    self.download_button.clicked.connect(lambda: self.download())

  def enabled_button(self, enabled):
    self.search_button.setEnabled(enabled)
    self.download_button.setEnabled(enabled)

  def search(self):
    self.mange.init(self.manga_search.text())
    title = self.main_config['General']['title']

    self.window.setWindowTitle(f'{title} | 接続準備中...')
    self.enabled_button(False)

    if self.mange.check():
      self.window.setWindowTitle(f'{title} | 接続成功')

      cover_url = self.mange.get_cover()
      self.cover_image.set_cover(cover_url)
    else:
      self.window.setWindowTitle(f'{title} | 接続エラー、再入力してください')
      self.cover_image.reset_cover()

    self.enabled_button(True)

  def download(self):
    download_path = QFileDialog.getExistingDirectory(
        self, 'フォルダ選択', )
    title = self.main_config['General']['title']

    self.enabled_button(False)

    if download_path:
      self.mange.download(download_path, self.window, title)

    self.window.setWindowTitle(f'{title} | ダウンロード完了')
    self.enabled_button(True)
