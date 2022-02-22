from . import translator as _
from .settings import telegram_clinet, translator


def main() -> None:
  telegram_clinet.start()
  telegram_clinet.loop.run_until_complete(translator.initialize())
  telegram_clinet.run_until_disconnected()


if __name__ == '__main__':
  main()
