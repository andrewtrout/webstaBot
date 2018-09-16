from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

KEYWORDS = ["modernart","artgallery","model","contemporaryart","oshitwaddup"] # Tags to follow

MY_USER = 'USERNAME' # Replace with your username
MY_PASSWORD = 'PASSWORD' # Replace with your password

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('window-size=1200x600')

browser = webdriver.Chrome('assets/chromedriver', chrome_options=options)
#browser.set_window_size(960,1170)


def whoMadeIt():
	print('''
		
  _      _________  _____________   ___  ____ ______                
 | | /| / / __/ _ )/ __/_  __/ _ | / _ )/ __ /_  __/                
 | |/ |/ / _// _  _\ \  / / / __ |/ _  / /_/ // /                   
 |__/|__/___/____/___/ /_/ /_/ |_/____/\____//_/ 

		CREATED BY:                                                                           
   ___   _  _____  ___  _____      __  _________  ____  __  ________
  / _ | / |/ / _ \/ _ \/ __| | /| / / /_  __/ _ \/ __ \/ / / /_  __/
 / __ |/    / // / , _/ _/ | |/ |/ /   / / / , _/ /_/ / /_/ / / /   
/_/ |_/_/|_/____/_/|_/___/ |__/|__/   /_/ /_/|_|\____/\____/ /_/    
		                                                                    

		''')



def logIn():

	browser.get('https://www.instagram.com/accounts/login/')

	time.sleep(1)

	email = browser.find_element_by_css_selector('input[aria-label="Phone number, username, or email"]')
	email.send_keys(MY_USER)
	pw = browser.find_element_by_css_selector('input[aria-label="Password"]')
	pw.send_keys(MY_PASSWORD, Keys.RETURN)

	print "logged in successfully!"
	
	time.sleep(1)



def scrape():

	for KEYWORD in KEYWORDS:
		#png = 1

		taglink = 'https://www.instagram.com/explore/tags/%s' % KEYWORD
		#browser.get('https://www.instagram.com/andrewtrout/saved/')

		browser.get(taglink)

		time.sleep(1)

		print("Finding images. Please wait...")

		# browser.execute_script("window.scrollBy(0, 1180);")

		# lastHeight = browser.execute_script("return document.body.scrollHeight")

		# for _ in range(3):
		#     browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		#     time.sleep(2)
		#     newHeight = browser.execute_script("return document.body.scrollHeight")

		# Get scroll height
		last_height = browser.execute_script("return document.body.scrollHeight")

		pictures = []
		counter = 0
		while counter < 100:
			# Scroll down to bottom
			browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

			# Wait to load page
			time.sleep(5)


			blocks = browser.find_elements_by_css_selector('.Nnq7C .v1Nh3 a')

			for block in blocks:
				i = block.get_attribute("href")
				if i not in pictures:
					pictures.append(i)

			# Calculate new scroll height and compare with last scroll height
			new_height = browser.execute_script("return document.body.scrollHeight")
			if new_height == last_height:
				break
			last_height = new_height
			counter+=1
			print counter
		for pic in pictures:
			browser.get(pic)
			time.sleep(1)

			try:
				name = browser.find_element_by_css_selector('.FPmhX').text
				img = browser.find_element_by_css_selector('.KL4Bh img').get_attribute('src')
				like = browser.find_element_by_css_selector('.fr66n button')

				time.sleep(2)

				like.click()
				print "Liked %s's picture!" % name
				time.sleep(2)

				#urllib.urlretrieve(img, 'img/videoScreenShot_' + str(name) + '_' + str(png) + '.png')
				#png+=1

			except:
				# name = browser.find_element_by_css_selector('.FPmhX').text
				# img = browser.find_element_by_css_selector('.KL4Bh img').get_attribute('src')
				# like = browser.find_element_by_css_selector('.fr66n button')

				# time.sleep(2)

				# like.click()
				# print "Liked %s's picture!" % name
				# time.sleep(2)
				print "error"

				#urllib.urlretrieve(img, 'img/videoScreenShot_' + str(name) + '_' + str(png) + '.png')
				#png+=1



	


whoMadeIt()

logIn()

scrape()



