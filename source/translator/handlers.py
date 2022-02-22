from .config import TARGET_LANGUAGE
from ..settings import telegram_clinet
from .translate_message import translate_message

from telethon import events
from telethon.tl.patched import Message
from telethon.events.newmessage import NewMessage
from telethon.events.messageedited import MessageEdited


@telegram_clinet.on(events.NewMessage(outgoing=True))
async def message_new(event: NewMessage.Event) -> None:
  message: Message = event.message
  await translate_message(message)


@telegram_clinet.on(events.MessageEdited(outgoing=True))
async def message_edit(event: MessageEdited.Event) -> None:
  message: Message = event.message
  await translate_message(message)


@telegram_clinet.on(events.NewMessage(func=lambda e: e.message.text.startswith('/target')))
async def target_command(event: NewMessage.Event) -> None:
  global TARGET_LANGUAGE

  message: Message = event.message
  message_text = message.text.replace('/target ', '')

  TARGET_LANGUAGE = message_text
  await message.delete()
