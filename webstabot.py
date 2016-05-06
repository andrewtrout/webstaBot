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

browser = webdriver.PhantomJS(service_log_path=os.path.devnull)
browser.set_window_size(960,1170)

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

	time.sleep(3)

	email = browser.find_element_by_css_selector('input[placeholder="Username"]')
	email.send_keys(MY_USER)
	pw = browser.find_element_by_css_selector('input[placeholder="Password"]')
	pw.send_keys(MY_PASSWORD, Keys.RETURN)

	print "logged in successfully!"
	
	time.sleep(1)


def scrape():

	png = 1

	for KEYWORD in KEYWORDS:

		taglink = 'https://www.instagram.com/explore/tags/%s' % KEYWORD
		browser.get(taglink)

		time.sleep(1)

		print("Liking tag " + KEYWORD)
		print("Finding images. Please wait...")

		browser.execute_script("window.scrollBy(0, 1180);")

		loadmore = browser.find_element_by_link_text('LOAD MORE')
		time.sleep(2)
		loadmore.click()

		lastHeight = browser.execute_script("return document.body.scrollHeight")

		for _ in range(20):
		    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		    time.sleep(2)
		    newHeight = browser.execute_script("return document.body.scrollHeight")

		#Un-comment the lines below to take a screenshot of everything you are liking
		
		#browser.save_screenshot('img/everything_' + str(png) + '.png')
		#png+=1

		pictures = []

		blocks = browser.find_elements_by_css_selector('._8mlbc._t5r8b')

		for block in blocks:
			i = block.get_attribute("href")
			pictures.append(i)

		for pic in pictures:
			browser.get(pic)
			time.sleep(.1)

			try:
				browser.find_element_by_link_text('Go back to Instagram.')
			except:

				name = browser.find_element_by_css_selector('._ook48').text
				like = browser.find_element_by_css_selector('._345gm')

				like.click()
				print "Liked %s's picture!" % name
				time.sleep(.1)

				#Un-comment the lines below to take a screenshot of every liked image

				#browser.save_screenshot('img/liked_img_' + str(png) + '.png')
				#png+=1


			browser.back()
			time.sleep(.1)

		print "LIKED EVERYTHING UNDER THE TAG '%s'" % KEYWORD





whoMadeIt()

logIn()

scrape()



