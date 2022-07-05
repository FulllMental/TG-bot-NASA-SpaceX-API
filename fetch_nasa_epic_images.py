import requests
import pathlib
import datetime
import os
from dotenv import load_dotenv


def download_nasa_epic(nasa_token):
    url = f'https://api.nasa.gov/EPIC/api/natural'
    payload = {"api_key": nasa_token}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    response_data = response.json()
    picture_names = [item["image"] for item in response_data]
    epic_dates = [(datetime.datetime.fromisoformat(item["date"])).strftime("%Y/%m/%d") for item in response_data]
    pathlib.Path(f'{directory}').mkdir(parents=True, exist_ok=True)

    for name_number, picture_date in enumerate(epic_dates):
        filename = f'{directory}/EPIC{name_number}.png'

        response_picture = requests.get(f'https://api.nasa.gov/EPIC/archive/natural/{picture_date}/png/{picture_names[name_number]}.png', params=payload)
        response_picture.raise_for_status()

        with open(filename, 'wb') as file:
            file.write(response_picture.content)


if __name__ == '__main__':
    directory = 'images'
    load_dotenv()
    nasa_token = os.getenv("NASA_TOKEN")
    download_nasa_epic(nasa_token)
