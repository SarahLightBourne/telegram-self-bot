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

  if message_text.startswith('/'):
    message_text, annotations = message_text[1:], True
  else:
    annotations = False

  translated_parts = await asyncio.gather(*[
    translator.translate(part, 'en', 'ja')
  for part in to_translate])

  data = list(zip(to_translate, translated_parts))

  for before, after in data:
    message_text = message_text.replace(f'[{before}]', after)

  if annotations:

    if len(to_translate) == 1:
      message_text = f'{message_text}\n\n\n<code>{before}</code>'
    else:
      words = '\n'.join(f'<code>{after}</code> <b>{before}</b>' for before, after in data)
      message_text = f'{message_text}\n\n{words}'

  await message.edit(message_text, parse_mode='HTML')
