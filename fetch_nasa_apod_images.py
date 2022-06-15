import requests
import pathlib
import os
from dotenv import load_dotenv
from os.path import splitext
from urllib.parse import unquote, urlsplit


def get_extension(NASA_picture_url):
    link_split = urlsplit(NASA_picture_url)
    file_name = unquote(link_split[2])
    file_extension = splitext(file_name)

    return file_extension[1]


def download_nasa_apod(NASA_picture_url, img_count):
    directory = "NASA"
    payload = {"count": img_count}
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


if __name__ == '__main__':
    load_dotenv()
    NASA_TOKEN = os.getenv("NASA_TOKEN")
    NASA_picture_url = f'https://api.nasa.gov/planetary/apod?api_key={NASA_TOKEN}'
    img_count = input('Сколько фото необходимо скачать: ')
    download_nasa_apod(NASA_picture_url, img_count)
