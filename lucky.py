# -*- coding: utf-8 -*-

import sys, requests, bs4, webbrowser

print ('Googling...')

res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
# try:
# 	res.raise_for_status()
# except:
# 	print('Can\'t search for' + ' '.join(sys.argv[1:]))
# else:
# 	print('Getting response')

google = bs4.BeautifulSoup(res.text, 'html.parser')

links = google.select('h3 a')
link = ''

numOfOpen = min(5, len(links))
# for i in range(numOfOpen):
# 	link = links[i].get('href').encode('utf-8').strip('True').strip('u\'/url?q=')
# 	print link
# 	webbrowser.open(link)

for i in range(numOfOpen):
	webbrowser.open('http://google.com' + links[i].get('href'))