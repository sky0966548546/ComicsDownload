import configparser


class Config:

  def __init__(self, setting_file=None):
    self.WINDOW = {
      'APP_NAME': '漫画ダウンローダー',
      'STYLE': 'Fusion',
      'WIDTH': 400,
      'HEIGHT': 500
    }

    self.WIDGET = {
      'BUTTON': {
        'SEARCH': '検索',
        'DOWNLOAD': 'ダウンロード',
        'PDF': 'として保存'
      },
      'FILEDIALOG': 'フォルダ選択'
    }

    self.MESSAGE = {
      'SEARCH': {
        'SEARCHING': f'{self.WINDOW['APP_NAME']} | 検索中...',
        'SUCCESS': f'{self.WINDOW['APP_NAME']} | 検索成功',
        'ERROR': f'{self.WINDOW['APP_NAME']} | 検索エラー、再入力してください',
      },
      'DOWNLOAD': {
        'DOWNLOADING': f'{self.WINDOW['APP_NAME']} | ダウンロード中...',
        'SUCCESS': f'{self.WINDOW['APP_NAME']} | ダウンロード完了',
        'ERROR': f'{self.WINDOW['APP_NAME']} | ダウンロードエラー、再入力してください'
      },
      'LOCKFILE': 'アプリケーションは既に実行中です。'
    }

    if setting_file:
      self.SETTING = configparser.ConfigParser()
      self.SETTING.read(setting_file)
    else:
      self.SETTING = None

    self.config = {
      'WINDOW': self.WINDOW,
      'WIDGET': self.WIDGET,
      'MESSAGE': self.MESSAGE,
      'SETTING': self.SETTING
    }

  def __getitem__(self, item):
    return self.config[item]
