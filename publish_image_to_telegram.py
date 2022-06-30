import telegram
import random
import time
import os
from dotenv import load_dotenv
from support_file import pictures, directory
from fetch_spacex_images import fetch_spacex_launch
from fetch_nasa_apod_images import download_nasa_apod
from fetch_nasa_epic_images import download_nasa_epic


def download_pictures():
    download_nasa_apod(nasa_token, img_count='3')
    download_nasa_epic(nasa_token)
    fetch_spacex_launch(launch_number='63')


def send_photo(picture):
    bot = telegram.Bot(token=telegram_bot_api)
    bot.send_photo(chat_id='@nasa_photo_lesson', photo=open(fr'{directory}\{picture}', 'rb'))


if __name__ == '__main__':
    load_dotenv()
    telegram_bot_api = os.getenv("TELEGRAM_BOT_API")
    nasa_token = os.getenv("NASA_TOKEN")
    time_limit = int(os.getenv("TIME_LIMIT"))
    download_pictures()
    while True:
        for picture in pictures:
            send_photo(picture)
            time.sleep(time_limit)
        random.shuffle(pictures)
