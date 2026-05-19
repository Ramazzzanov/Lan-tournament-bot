
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

tournaments = [
    {
        "game": "CS2",
        "title": "CS2 Mini LAN #1",
        "date": "2026-06-01"
    },
    {
        "game": "Dota 2",
        "title": "Dota LAN Cup",
        "date": "2026-06-05"
    },
]

@router.message(Command("tournaments"))
async def show_tournaments(message: Message):
    text = "<b>Active tournaments:</b>\n\n"

    for t in tournaments:
        text += (
            f"🎮 {t['title']}\n"
            f"Game: {t['game']}\n"
            f"Date: {t['date']}\n\n"
        )

    await message.answer(text)
