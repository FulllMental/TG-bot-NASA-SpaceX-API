import telegram
import random
import time
from support_file import choose_file, telegram_bot_api, nasa_token, time_limit, directory
from fetch_spacex_images import fetch_spacex_launch
from fetch_nasa_apod_images import download_nasa_apod
from fetch_nasa_epic_images import download_nasa_epic


def download_pictures():
    download_nasa_apod(img_count='3')
    download_nasa_epic(nasa_token)
    fetch_spacex_launch(launch_number='63')


def send_photo(picture):
    bot = telegram.Bot(token=telegram_bot_api)
    bot.send_photo(chat_id='@nasa_photo_lesson', photo=open(fr'{directory}\{picture}', 'rb'))


if __name__ == '__main__':
    download_pictures()
    pictures_list = choose_file()
    while True:
        for picture in pictures_list:
            send_photo(picture)
            time.sleep(time_limit)
        random.shuffle(pictures_list)
