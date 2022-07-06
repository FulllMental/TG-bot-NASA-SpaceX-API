import requests
import pathlib


def fetch_spacex_launch(directory, launch_number):
    url = f"https://api.spacexdata.com/v3/launches/{launch_number}"
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


if __name__ == '__main__':
    directory = 'images'
    launch_number = input('Введите номер запуска SpaceX: ')
    fetch_spacex_launch(directory, launch_number)
