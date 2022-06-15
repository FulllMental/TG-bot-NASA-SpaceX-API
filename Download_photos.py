import requests
import pathlib
import datetime
import os
from dotenv import load_dotenv
from os.path import splitext
from urllib.parse import unquote, urlsplit


def download_hubble_picture(directory, hubble_picture_url):
    pathlib.Path(f'{directory}').mkdir(parents=True, exist_ok=True)
    filename = f'{directory}/hubble.jpeg'

    response = requests.get(hubble_picture_url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)


def fetch_spacex_launch(directory):
    url = "https://api.spacexdata.com/v3/launches/67"
    response_links = requests.get(url)
    response_links.raise_for_status()
    spacex_links = response_links.json()["links"]["flickr_images"]
    pathlib.Path(f'{directory}').mkdir(parents=True, exist_ok=True)

    for name_number, picture_url in enumerate(spacex_links):
        filename = f'{directory}/spacex{name_number}.jpg'

        response_picture = requests.get(picture_url)
        response_picture.raise_for_status()

        with open(filename, 'wb') as file:
            file.write(response_picture.content)


def get_extension(NASA_picture_url):
    link_split = urlsplit(NASA_picture_url)
    file_name = unquote(link_split[2])
    file_extension = splitext(file_name)

    return file_extension[1]


def download_NASA_APOD(NASA_picture_url):
    directory = "NASA"
    payload = {"count": "3"}
    response_links = requests.get(NASA_picture_url, params=payload)
    response_links.raise_for_status()
    NASA_links = [link["url"] for link in response_links.json()]
    pathlib.Path(f'{directory}').mkdir(parents=True, exist_ok=True)

    for name_number, picture_url in enumerate(NASA_links):
        extension = get_extension(picture_url)
        filename = f'{directory}/NASA{name_number}{extension}'

        response_picture = requests.get(picture_url)
        response_picture.raise_for_status()

        with open(filename, 'wb') as file:
            file.write(response_picture.content)


def download_NASA_EPIC(NASA_TOKEN):
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
    directory = 'images'
    hubble_picture_url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    NASA_picture_url = f'https://api.nasa.gov/planetary/apod?api_key={NASA_TOKEN}'
    download_hubble_picture(directory, hubble_picture_url)
    fetch_spacex_launch(directory)
    download_NASA_APOD(NASA_picture_url)
    download_NASA_EPIC(NASA_TOKEN)
