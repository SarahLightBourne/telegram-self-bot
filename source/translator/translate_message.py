from ..settings import translator
from telethon.tl.patched import Message

import asyncio
from re import compile

message_regex = compile(r'\[([^\]]+)\]')


async def translate_message(message: Message) -> None:
  message_text = message.text
  to_translate = message_regex.findall(message_text)

  if not to_translate:
    return

  translated_parts = await asyncio.gather(*[
    translator.translate(part, 'en', 'ja')
  for part in to_translate])

  for before, after in zip(to_translate, translated_parts):
    message_text = message_text.replace(f'[{before}]', after)

  await message.edit(message_text)
