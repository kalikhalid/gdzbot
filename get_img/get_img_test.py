import requests
from requests.adapters import HTTPAdapter
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse
from urllib3.util.retry import Retry
import os
from tqdm import tqdm
import sys

def get_all_images(url):
	soup = bs(requests.get(url).content, "html.parser")
	urls = []
	for img in soup.find_all("img"):
		img_url = img.attrs.get("src")
		if not img_url:
		    continue
		img_url = urljoin(url, img_url)
		if "avatars" in img_url.split("/"):
			continue
		try:
			pos = img_url.index("?")
			img_url = img_url[:pos]
		except ValueError:
			pass
		urls.append(img_url)
	return urls
def download_imgs(url, path, filedir):
	if not os.path.isdir(filedir + '/' + path):
		os.makedirs(filedir + '/' + path)
	session = requests.Session()
	retry = Retry(connect=3, backoff_factor=0.5)
	adapter = HTTPAdapter(max_retries=retry)
	session.mount('http://', adapter)
	session.mount('https://', adapter)
	
	response = session.get(url, stream=True)
	file_size = int(response.headers.get("Content-Length", 0))
	filename = os.path.join(path, url.split("/")[-1])
	with open(filedir + '/' + filename, "wb") as f:
		for data in response.iter_content(1024):
			f.write(data)

def get_images(url, pathname, filedir):
	imgs = get_all_images(url)
	for img in imgs:
		download_imgs(img, pathname, filedir=filedir)
	thisfiledir = filedir + '/' + pathname
	os.chdir(filedir + '/' + pathname)
	deletefilearr = ['crown.svg',
		'logo.png',
		'buy.png',
		'loader.gif',
		'popup-close.png',
		'popup-close-white.png',
		'user-icon.png',
		'vk-button-icon.png',
		'38950965',
		'icon_arrow.png',
		'ajax.gif',
		'63ce6811e72f87.79737820.jpg',
		'63eef4e60dbc01.77693910.jpg',
		'63ff8e24af55e9.52781388.jpg',
		'635b6ab44ceac0.05938854.jpg',
		'640096142ffc03.78465748.jpg',
		'star-icon.svg'
	]
	for i in deletefilearr:
		try:
			os.remove(thisfiledir + '/' + str(i))
		except FileNotFoundError:
 			pass
# get_images("https://gdz.ru/class-5/geografiya/konturnie-karti-matveev/2-s/", 'test', "/home/botenter/get_img/")