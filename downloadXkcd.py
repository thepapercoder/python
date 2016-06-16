#downloadXkcd.py - Download every single XKCD comic

import requests, os, bs4

url = 'http://xkcd.com'

os.makedirs('xkcd') 

while not url.endswith('#'):
	#TODO: Download the page
	print('Downloading page %s...' % url)
	res = requests.get(url)
	res.raise_for_status()

	soup = bs4.BeautifulSoup(res.text, 'html.parser')

	#TODO: Find the URL of the comic image
	#TODO: Download the image
	comicElem = soup.select('#comic img')
	if (comicElem) == []:
		print('Can\'t find comic image')
	else:
		try:
			comicURL = 'http:' + comicElem[0].get('src')
			#Download the image:
			print('Downloading image %s...' % comicURL)
			res = requests.get(comicURL)
			res.raise_for_status()

		except requests.exceptions.MissingSchema:
			#skip this comic
			prevLink = soup.select('a[rel="prev"]')[0]
			url = 'http://xkcd.com' + prevLink.get('href')
			continue

	#TODO: Save the image to ./xkcd
	imageFile = open(os.path.join('xkcd', os.path.basename(comicURL)), 'wb')
	for chunk in res.iter_content(100000):
		imageFile.write(chunk)
	imageFile.close()

	#TODO: Get the prev button's url
	prevLink = soup.select('a[rel="prev"]')[0]
	url = 'http://xkcd.com' + prevLink.get('href')

print ('Done.')