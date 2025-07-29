from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message
from config.config import logger

common_router = Router()

@common_router.message(Command("start"))
async def handle_start(message: Message):
    logger.info(f"Received /start command from user: {message.from_user.id} ({message.from_user.full_name})")
    response_text = (
                    f"Hello!\n" 
                    f"Your ID is: <code>{message.from_user.id}</code>"
    )

    await message.answer(response_text, parse_mode="HTML")


@common_router.my_chat_member(F.new_chat_member.is_member | F.new_chat_member.status == "member")
async def handle_group_joined(event: types.ChatMemberUpdated):
    logger.info(f"User {event.from_user.id} ({event.from_user.full_name}) joined the group {event.chat.title} ({event.chat.id})")
    response_text = (
                    f"Hello!\n"
                    f"Group ID is: <code>{event.chat.id}</code>\n"
                    f"Your id is: <code>{event.from_user.id}</code>"
    )

    await event.answer(response_text, parse_mode="HTML")


@common_router.message(Command("id"))
async def handle_text_message(message: Message):
    logger.info(f"Received text message from user: {message.from_user.id} ({message.from_user.full_name}) in chat: {message.chat.id} ({message.chat.title})")
    chat = message.chat
    if chat.type == "group":
        response_text = (
            f"Group ID is: <code>{chat.id}</code>\n"
            f"Your id is: <code>{message.from_user.id}</code>"
        )

        await message.answer(response_text, parse_mode="HTML")
        
    else:
        response_text = (
                   f"Your id is: <code>{message.from_user.id} </code>"
        )

        await message.answer(response_text, parse_mode="HTML")

@common_router.message(F.forward_from | F.forward_from_chat)
async def handle_forwarded_message(message: Message):
    logger.info(f"Received forwarded message from user: {message.from_user.id} ({message.from_user.full_name}) in chat: {message.chat.id} ({message.chat.title})")
    response_text = ""

    if message.forward_from:
        user = message.forward_from
        response_text = (
            f"Forwarded from user: <code>{user.id}</code> ({user.full_name})\n"
            f"User ID: <code>{user.id}</code>\n"
        )

        await message.answer(response_text, parse_mode="HTML")

    elif message.forward_from_chat:
        chat = message.forward_from_chat
        chat_type = "Group" if chat.type == "group" else "Channel" if chat.type == "channel" else "Private"
        response_text = (
            f"Forwarded from {chat_type}: {chat.title}\n"
            f"Chat ID: <code>{chat.id}</code>\n"
        )

        await message.answer(response_text, parse_mode="HTML")