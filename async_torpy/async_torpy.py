from utils import info
from subprocess import Popen, PIPE

import asyncio
from typing import Tuple, Union


class Tor:
  index = 0

  def __init__(self) -> None:
    self.index += 1

    self.process = None
    self.socks = 9000 + self.index
    self.control = 9050 + self.index

  async def _wait_until_launched(self) -> None:
    for line in self.process.stdout:
      await asyncio.sleep(0)

      if 'Bootstrapped 100%' in str(line):
        return info('info', 'Tor is started')

  async def __aenter__(self, *args: Tuple) -> Union[str, None]:
    info('info', 'Tor requested')
    if self.process: return

    self.process = Popen(
      f'tor --SOCKSPort {self.socks} --ControlPort {self.control} CookieAuthentication 1',
      stdout=PIPE,
      shell=True
    )

    await self._wait_until_launched()
    return f'socks5://127.0.0.1:{self.socks}'

  async def __aexit__(self, *args: Tuple) -> None:
    self.process.kill()
    self.process = None
    info('info', 'Tor is finished')
