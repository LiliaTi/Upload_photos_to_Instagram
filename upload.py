from instabot import Bot
from pathlib import Path
import os
from dotenv import load_dotenv


if __name__ == '__main__':
	load_dotenv()
	username = os.getenv("INSTA_LOGIN")
	password = os.getenv("INSTA_PASSWORD")
	path = Path.home() / 'PythonProjects' / 'Upload_photos_to_Instagram' / 'Images' 
	
	bot = Bot()
	bot.login(username=username, password=password)

	images = os.listdir('Images')

	for image in images:
		bot.upload_photo(path / image)
