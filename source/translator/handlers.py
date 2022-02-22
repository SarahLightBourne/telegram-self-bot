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
