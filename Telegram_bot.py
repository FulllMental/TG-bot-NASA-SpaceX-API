import telegram
import os
from dotenv import load_dotenv


def bot_message():
    bot = telegram.Bot(token=os.getenv("TELEGRAM_BOT_API"))
    bot.send_message(chat_id='@nasa_photo_lesson', text='Hello!')


if __name__ == '__main__':
    load_dotenv()
    bot_message()
