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


def send_photo(picture, api_bot_token):
    with open(fr'{directory}\{picture}', 'rb') as photo:
        bot = telegram.Bot(token=api_bot_token)
        bot.send_photo(chat_id=chat_id, photo=photo)


if __name__ == '__main__':
    load_dotenv()
    chat_id = os.getenv("CHAT_ID")
    api_bot_token = os.getenv("API_BOT_TOKEN")
    nasa_token = os.getenv("NASA_TOKEN")
    time_limit = int(os.getenv("TIME_LIMIT"))
    download_pictures()
    while True:
        for picture in pictures:
            send_photo(picture, api_bot_token)
            time.sleep(time_limit)
        random.shuffle(pictures)

