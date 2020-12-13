import requests
from PIL import Image
import os


def prepare_image_for_instagram(image_name, path):
    image = Image.open(path / image_name)
    image.thumbnail((1080, 1080))
    image_name_parts = image_name.split('.')
    if image_name_parts[-1] != 'jpg':
        new_image_name = image_name_parts[0]
        image.save(path / f'{new_image_name}.jpg', format="JPEG")
        os.remove(path / image_name)
    else:
        image.save(path / image_name)


def load_image(image_name, url, path):
    response = requests.get(url, verify=False)
    response.raise_for_status()
    with open(path / image_name, 'wb') as file:
        file.write(response.content)
