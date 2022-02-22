''' Module for colored output '''

from sys import exit as program_exit
from colorama import Style, Fore, init
init(autoreset=True); init(wrap=False)


def info(label: str, message: str) -> None:
  print(f'{Fore.CYAN}[{Fore.MAGENTA}{label}{Fore.CYAN}] {Style.BRIGHT}{Fore.GREEN}➜{Style.NORMAL}{Fore.CYAN} {message}')


def error(label: str, message: str) -> None:
  print(f'{Fore.CYAN}[{Fore.RED}{label}{Fore.CYAN}] {Style.BRIGHT}{Fore.RED}➜{Style.NORMAL}{Fore.CYAN} {message}')


def fatal(label: str, message: str) -> None:
  print(f'{Fore.CYAN}[{Fore.RED}{label}{Fore.CYAN}] {Style.BRIGHT}{Fore.RED}➜{Style.NORMAL}{Fore.CYAN} {message}')
  program_exit(1)
