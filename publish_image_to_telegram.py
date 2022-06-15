import telegram
import os
from dotenv import load_dotenv
from choose_file import choose_file

def bot_message():
    directory, picture = choose_file()
    bot = telegram.Bot(token=os.getenv("TELEGRAM_BOT_API"))
    bot.send_photo(chat_id='@nasa_photo_lesson', photo=open(f'{directory}\{picture}', 'rb'))


if __name__ == '__main__':
    load_dotenv()
    bot_message()
