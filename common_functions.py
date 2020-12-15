import requests
from PIL import Image
import os


def prepare_image_for_instagram(image_name, path):
    image = Image.open(path / image_name)
    image.thumbnail((1080, 1080))
    short_image_name, extension = os.path.splitext(image_name)
    if extension != '.jpg':
        image.save(path / f'{short_image_name}.jpg', format="JPEG")
        os.remove(path / image_name)
    else:
        image.save(path / image_name)


def load_image(image_name, url, path):
    response = requests.get(url, verify=False)
    response.raise_for_status()
    with open(path / image_name, 'wb') as file:
        file.write(response.content)
