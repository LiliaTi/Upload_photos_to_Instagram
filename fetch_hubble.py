import requests
from pathlib import Path
from fetch_spacex import load_image, prepare_image_for_Instagram


def image_extension(link_of_image):
	return link_of_image.split('.')[-1]


def load_hubble_image(image_id, path):
	url = 'http://hubblesite.org/api/v3/image/{}'.format(image_id)
	response = requests.get(url)
	response.raise_for_status()
	image_info = response.json()['image_files']
	links = [item['file_url'] for item in image_info]
	link = 'https:' + links[-1]
	filename = str(image_id) + '.' + image_extension(link)
	load_image(filename, link, path)
	prepare_image_for_Instagram(filename, path)

	


def load_hubble_collection(collection_name, path):
	url = 'http://hubblesite.org/api/v3/images?page=all&collection_name={}'.format(collection_name)
	response = requests.get(url)
	response.raise_for_status()
	ids = [item['id'] for item in response.json()]
	for id in ids:
		load_hubble_image(id, path)
		
		

if __name__ == '__main__':
	
	path = Path.home() / 'PythonProjects' / 'Upload_photos_to_Instagram' / 'Images' 
	path.mkdir(parents=True, exist_ok=True)

	load_hubble_collection('news', path)
