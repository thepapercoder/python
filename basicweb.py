# -*- coding: utf-8 -*-
import requests, bs4

res = requests.get('http://youtube.com')
vnex = bs4.BeautifulSoup(res.text, 'html.parser')

type(vnex)
links = vnex.select('h3 > a')

listOfLink =''

for link in links:
	listOfLink += '\n' + link.getText().encode('utf-8')
	print (link.getText().encode('utf-8') + '\n')

print listOfLink

