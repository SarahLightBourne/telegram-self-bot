''' Module for making sync operations async '''

from asyncio import to_thread
from typing import Callable, Coroutine, Any


def sync_to_async(function: Callable) -> Coroutine:

  async def wrapper(*args: tuple, **kwargs: dict) -> Any:
    return await to_thread(function, *args, **kwargs)

  return wrapper
