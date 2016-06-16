# -*- coding: utf-8 -*-
import pyperclip

text = pyperclip.paste()

text = text.strip()

#cắt dòng
line = text.split('\n')

for i in range(len(line)):
	line[i] = '* ' + line[i]

pyperclip.copy(text) 