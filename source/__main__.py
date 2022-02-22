from .settings import telegram_clinet
from .settings import translator


async def main() -> None:
  await translator.initialize()
  await telegram_clinet.send_message('me', 'Hello There')


if __name__ == '__main__':
  telegram_clinet.start()
  telegram_clinet.loop.run_until_complete(main())
  telegram_clinet.run_until_disconnected()
