# -*- coding: utf-8 -*-
import urllib

url = "http://www.dantri.com"

handle = urllib.urlopen(url)

print (str(handle.read()))