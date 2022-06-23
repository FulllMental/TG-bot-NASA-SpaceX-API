import requests
import pathlib
import datetime
from support_file import nasa_token, directory


def download_nasa_epic(nasa_token):
    url = f'https://api.nasa.gov/EPIC/api/natural?api_key={nasa_token}'
    response_links = requests.get(url)
    response_links.raise_for_status()
    picture_names = [item["image"] for item in response_links.json()]

    epic_dates = [(datetime.datetime.fromisoformat(item["date"])).strftime("%Y/%m/%d") for item in response_links.json()]
    pathlib.Path(f'{directory}').mkdir(parents=True, exist_ok=True)

    for name_number, picture_date in enumerate(epic_dates):
        filename = f'{directory}/EPIC{name_number}.png'

        response_picture = requests.get(f'https://api.nasa.gov/EPIC/archive/natural/{picture_date}/png/{picture_names[name_number]}.png?api_key={nasa_token}')
        response_picture.raise_for_status()

        with open(filename, 'wb') as file:
            file.write(response_picture.content)


if __name__ == '__main__':
    download_nasa_epic(nasa_token)
