import os
import re
import time
from urllib import request, error
from bs4 import BeautifulSoup as bs


class Manga:

  def __init__(self, main_config):
    self.mange_id = None
    self.origin = None
    self.soup = None
    self.main_config = main_config

    self.headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
    }

  def init(self, mange_id):
    self.mange_id = mange_id
    self.origin = f'https://nhentai.net/g/{self.mange_id}'

  def init_error(self):
    self.mange_id = '371601'
    self.origin = f'https://nhentai.net/g/{self.mange_id}'

  def check(self):
    req = request.Request(url=self.origin, headers=self.headers)

    try:
      response = request.urlopen(req)
      self.soup = bs(response.read().decode('utf-8'), 'html.parser')

      return True
    except error.HTTPError:
      self.init_error()
      self.check()

      return False

  def get_cover(self):
    cover_element = self.soup.find(id='cover')
    cover_tag = cover_element.find('img')

    return cover_tag['data-src']

  def get_title(self):
    title_element = self.soup.find('h2', class_='title')
    title_element = title_element.find_all('span')

    return ''.join(span.get_text() for span in title_element)

  def download(self, download_path, window, title):
    thumbnailContainer = self.soup.find(id='thumbnail-container')

    download_folder = re.sub(r'[<>|\|*|"|\/|\|:|?]', ' ', self.get_title())
    download_path = os.path.join(download_path, download_folder)

    if os.path.exists(download_path):
      return
    else:
      os.makedirs(download_path)

    if thumbnailContainer:
      image_list = []
      image_element = thumbnailContainer.find_all('img', class_='lazyload')

      for image in image_element:
        src = image['data-src']
        ext = src.split('.')[-1]

        src = src.replace(f't.{ext}', f'.{ext}')
        src = src.replace('https://t', 'https://i')

        image_list.append(src)

        image_list_length = len(image_list)

      for index, src in enumerate(image_list):
        ext = src.split('.')[-1]
        image_index = str(index + 1).zfill(len(str(image_list_length)))

        image_name = f'{image_index}.{ext}'
        image_name = re.sub(r'[<>|\|*|"|\/|\|:|?]', '_', image_name)

        image_list[index] = {'name': image_name, 'src': src}
        image_path = os.path.join(download_path, image_name)

        window.setWindowTitle(f'{title} | ダウンロード中...')

        request.urlretrieve(src, image_path)
        time.sleep(0.2)
