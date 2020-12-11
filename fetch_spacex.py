import requests
from pathlib import Path
from PIL import Image
import os


def prepare_image_for_Instagram(image_name,path):
	image = Image.open(path / image_name)
	image.thumbnail((1080, 1080))
	image_name_parts = image_name.split('.')
	if image_name_parts[-1] != 'jpg':
		new_image_name = image_name_parts[0]
		image.save(path / (new_image_name + '.' + 'jpg'), format="JPEG")
		os.remove(path / image_name)
	else:
		image.save(path / image_name)



def load_image(image_name, url, path):
    response = requests.get(url, verify=False)
    response.raise_for_status()
    with open(path / image_name, 'wb') as file:
	    file.write(response.content)
    

def fetch_spacex_last_launch(path):
	SpaceX_url = 'https://api.spacexdata.com/v4/launches/latest'
	response = requests.get(SpaceX_url)
	response.raise_for_status()
	SpaceX_links = response.json()['links']['flickr']['original']
	for link_number, link in enumerate(SpaceX_links):
		filename = 'spacex{}.jpg'.format(link_number + 1)
		load_image(filename, link, path)
		prepare_image_for_Instagram(filename, path)
		

if __name__ == '__main__':
	
	path = Path.home() / 'PythonProjects' / 'Upload_photos_to_Instagram' / 'Images' 
	path.mkdir(parents=True, exist_ok=True)

	fetch_spacex_last_launch(path)
