
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    text = (
        "🔥 Welcome to LAN Tournament Bot\n\n"
        "Games:\n"
        "• PUBG\n"
        "• Dota 2\n"
        "• CS2\n\n"
        "Commands:\n"
        "/tournaments - active tournaments"
    )

    await message.answer(text)
