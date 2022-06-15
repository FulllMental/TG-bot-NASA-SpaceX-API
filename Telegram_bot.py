import telegram
import os
from dotenv import load_dotenv


def bot_message():
    bot = telegram.Bot(token=os.getenv("TELEGRAM_BOT_API"))
    bot.send_photo(chat_id='@nasa_photo_lesson', photo=open('images/hubble.jpeg', 'rb'))


if __name__ == '__main__':
    load_dotenv()
    bot_message()
