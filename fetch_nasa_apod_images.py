import requests
import pathlib
import os
from dotenv import load_dotenv
from support_file import directory
from os.path import splitext
from urllib.parse import unquote, urlsplit


def get_extension(nasa_picture_url):
    link_split = urlsplit(nasa_picture_url)
    file_name = unquote(link_split[2])
    file_extension = splitext(file_name)

    return file_extension[1]


def download_nasa_apod(nasa_token, img_count):
    nasa_picture_url = f'https://api.nasa.gov/planetary/apod?api_key={nasa_token}'
    payload = {"count": img_count}
    response_links = requests.get(nasa_picture_url, params=payload)
    response_links.raise_for_status()
    nasa_links = [link["url"] for link in response_links.json()]
    pathlib.Path(f'{directory}').mkdir(parents=True, exist_ok=True)

    for name_number, picture_url in enumerate(nasa_links):
        extension = get_extension(picture_url)
        filename = f'{directory}/NASA{name_number}{extension}'

        response_picture = requests.get(picture_url)
        response_picture.raise_for_status()

        with open(filename, 'wb') as file:
            file.write(response_picture.content)


if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.getenv("NASA_TOKEN")
    img_count = input('Сколько фото необходимо скачать: ')
    download_nasa_apod(nasa_token, img_count)
