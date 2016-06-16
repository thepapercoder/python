# Auto Play 2048

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random, re


# Regular Ex for finding score
scoreRegex = re.compile(r'\d+')

# Open browser
browser = webdriver.Chrome()
browser.get('https://gabrielecirulli.github.io/2048/')
body = browser.find_element_by_tag_name('body')

#m Make a random move
def rand_key():
	num = random.randint(1,4)

	if num == 1:
		body.send_keys(Keys.DOWN)
	elif num == 2:
		body.send_keys(Keys.UP)
	elif num == 3:
		body.send_keys(Keys.LEFT)
	else:
		body.send_keys(Keys.RIGHT)

# Play the game... sit back and enjoy
def game(times):
	while times > 0:
		print(times)

		retry_button = browser.find_element_by_class_name('retry-button')

		while retry_button.is_displayed() == False:
			rand_key()

		scoreElem = browser.find_element_by_class_name('score-container')
		scoreStr = scoreElem.get_attribute('outerHTML')
		score = scoreRegex.search(scoreStr)

		print ('Your score is: ' + score.group(0))

		retry_button.click()

		times-=1

# Start the game
game(5)