import requests
from pathlib import Path
from common_functions import load_image, prepare_image_for_instagram


def fetch_spacex_last_launch(path):
    SpaceX_url = 'https://api.spacexdata.com/v4/launches/latest'
    response = requests.get(SpaceX_url)
    response.raise_for_status()
    spacex_links = response.json()['links']['flickr']['original']
    for link_number, link in enumerate(spacex_links):
        filename = 'spacex{}.jpg'.format(link_number + 1)
        load_image(filename, link, path)
        prepare_image_for_instagram(filename, path)


if __name__ == '__main__':

    path = Path.home() / 'Images'
    path.mkdir(parents=True, exist_ok=True)

    fetch_spacex_last_launch(path)
