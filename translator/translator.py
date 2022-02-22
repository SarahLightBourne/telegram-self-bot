from .driver import Driver

from httpx import AsyncClient
from fake_headers import Headers


class Translator:
  DETECT_URL = 'https://translate.yandex.net/api/v1/tr.json/detect'
  TRANSLATE_URL = 'https://translate.yandex.net/api/v1/tr.json/translate'

  def __init__(self, path: str) -> None:
    self.params = None
    self.requests_session = None
    self.driver = Driver(self, path)

  async def update_requests_session(self) -> None:
    self.requests_session = self.requests_session or AsyncClient()

  async def initialize(self) -> None:
    await self.driver.initialize()

  async def detect(self, text: str) -> str:
    await self.update_requests_session()

    params = {
      'sid': self.params['detect'],
      'srv': 'tr-text',
      'text': text
    }

    response = await self.requests_session.get(self.DETECT_URL, params=params, headers=Headers().generate())
    return response.json()['lang']

  async def translate(self, text: str, lang: str, target: str) -> str:
    await self.update_requests_session()

    params = {
      'id': self.params['translate'],
      'srv': 'tr-text',
      'lang': f'{lang}-{target}'
    }

    payload = {
      'text': text,
      'options': '4'
    }

    response = await self.requests_session.post(self.TRANSLATE_URL, params=params, data=payload, headers=Headers().generate())
    print(response.text)

  async def close(self) -> None:
    if self.requests_session:
      await self.requests_session.aclose()

    self.driver.close()
