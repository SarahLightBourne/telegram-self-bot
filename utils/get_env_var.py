''' Module for getting env vars '''

from os import environ
from .colored import fatal


def get_env_var(var_name: str) -> str:

  if var_name in environ:
    return environ[var_name]

  fatal(var_name, "Environment variable doesn't exist")
