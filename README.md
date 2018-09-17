  
### webstaBot

WebstaBot is a Instagram bot that uses Selenium to like user's posts based on the tags you choose. 


Requires Selenium as well as the Chrome driver which can be downloaded to the assets folder by following the steps below.

```
$ latest_version=$(wget https://chromedriver.storage.googleapis.com/LATEST_RELEASE -O -)
$ wget https://chromedriver.storage.googleapis.com/${latest_version}/chromedriver_linux64.zip
$ unzip chromedriver_linux64
$ mv chromedriver webstabot/assets/chromedriver
$ chmod +x webstaBot/assets/chromedriver
$ chmod 755 webstaBot/assets/chromedriver
$ cd webstaBot
``` 

Replace the information in webstabot.py listed below with your own.

KEYWORDS = ["modernart","artgallery","model","contemporaryart","oshitwaddup"] # Tags to follow

MY_USER = 'USERNAME' # Replace with your username

MY_PASSWORD = 'PASSWORD' # Replace with your password

Then run "python webstabot.py" and that's it!


