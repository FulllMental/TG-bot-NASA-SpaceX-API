import os
from dotenv import load_dotenv
load_dotenv()
telegram_bot_api = os.getenv("TELEGRAM_BOT_API")
nasa_token = os.getenv("NASA_TOKEN")
time_limit = int(os.getenv("TIME_LIMIT"))
directory = 'images'


def choose_file():
    response = [i for i in os.walk(fr'{os.getcwd()}\{directory}')]
    pictures_list = response[0][2]
    return pictures_list
