import requests
import pathlib
import datetime
import os
from dotenv import load_dotenv


def download_nasa_epic(NASA_TOKEN):
    url = f'https://api.nasa.gov/EPIC/api/natural?api_key={NASA_TOKEN}'
    directory = "EPIC"
    response_links = requests.get(url)
    response_links.raise_for_status()
    EPIC_picture_names = [item["image"] for item in response_links.json()]

    EPIC_dates = [(datetime.datetime.fromisoformat(item["date"])).strftime("%Y/%m/%d") for item in response_links.json()]
    pathlib.Path(f'{directory}').mkdir(parents=True, exist_ok=True)

    for name_number, picture_date in enumerate(EPIC_dates):
        filename = f'{directory}/EPIC{name_number}.png'

        response_picture = requests.get(f'https://api.nasa.gov/EPIC/archive/natural/{picture_date}/png/{EPIC_picture_names[name_number]}.png?api_key={NASA_TOKEN}')
        response_picture.raise_for_status()

        with open(filename, 'wb') as file:
            file.write(response_picture.content)

if __name__ == '__main__':
    load_dotenv()
    NASA_TOKEN = os.getenv("NASA_TOKEN")
    download_nasa_epic(NASA_TOKEN)