
import sqlite3
from vkbottle.bot import Bot, Message
from config import token
from vkbottle import Keyboard, Text
from vkbottle import GroupEventType, GroupTypes, Keyboard, Callback, VKAPIError
from vkbottle import Keyboard, KeyboardButtonColor, Text
from vkbottle.tools import DocMessagesUploader, PhotoMessageUploader

bot = Bot(token=token)

conn = sqlite3.connect('DB.db', check_same_thread=False)
cursor = conn.cursor()

def db_user(User_id: int, nick: str, Persons: int, Planet: str, lvl: int, Hero:  str, balance: int):
    cursor.execute('INSERT INTO user (User_id, nick, Persons, Planet, lvl, Hero, balance) VALUES (?, ?, ?, ?, ?, ?, ?)', (User_id, nick, Persons, Planet, lvl, Hero, balance))
    conn.commit()