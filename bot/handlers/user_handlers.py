from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from bot.controllers import create_user

router = Router()


@router.message(Command('start'))
async def cmd_start(msg: Message):
    user_id = str(msg.from_user.id)
    user_name = msg.from_user.first_name
    username = msg.from_user.username
    user_surname = msg.from_user.last_name
    await create_user(user_id=user_id, user_name=user_name, username=username, user_surname=user_surname)

