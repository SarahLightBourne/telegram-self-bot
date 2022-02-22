import re
import asyncio
import aioschedule

from async_torpy import Tor
from utils import sync_to_async

import time
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from typing import Dict
from pathlib import Path


class Driver:
  id_regex = re.compile(r'id=([^&]+)')

  def __init__(self, translator: object, path: Path) -> None:
    self.tor, self.translator, self.path = Tor(), translator, path

  async def initialize(self) -> None:
    await self.get_params()
    self.task = asyncio.create_task(self.pending())

  async def pending(self) -> None:
    aioschedule.every(15).minutes.do(self.get_params)

    while True:
      await asyncio.sleep(1)
      await aioschedule.run_pending()

  async def get_params(self) -> None:
    async with self.tor as proxy:
      self.translator.params = await self._get_params(proxy)

  @sync_to_async
  def _get_params(self, proxy: str) -> Dict:
    options = Options()
    options.add_argument('--headless')

    driver = webdriver.Chrome(self.path, seleniumwire_options=self.get_options(proxy), options=options)
    driver.get('https://translate.yandex.com')
    time.sleep(2)

    text_input = driver.find_element(By.ID, 'fakeArea')

    try:
      text_input.send_keys('Hello')
    except:
      time.sleep(5)
      text_input = driver.find_element(By.ID, 'fakeArea')
      text_input.send_keys('Hello')

    while driver.find_element(By.ID, 'translation').text == '':
      time.sleep(0.5)

    for request in driver.requests:
      if request:

        if request.url.startswith('https://translate.yandex.net/api/v1/tr.json/detect'):
          detect_sid = request.params['sid']

        elif request.url.startswith('https://translate.yandex.net/api/v1/tr.json/translate'):
          translate_id = self.id_regex.findall(request.url)[0]

    return {'detect': detect_sid, 'translate': translate_id}

  def get_options(self, proxy: str) -> Dict:
    return {
      'proxy': {
        'http': proxy,
        'https': proxy
      }
    }

  def close(self) -> None:
    if self.task:
      self.task.cancel()
