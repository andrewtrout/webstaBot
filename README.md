  
### webstaBot

WebstaBot is a Instagram bot that uses Selenium to like user's posts based on the tags you choose. 


Requires Selenium as well as the Chrome driver which can be downloaded to the assets folder by following the steps below.

### Selenium install

```
$ cd ~
$ sudo pip install selenium
```

### Chrome-stable install

```
$ cd ~
$ wget "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"
$ sudo dpkg -i google-chrome-stable_current_amd64.deb
$ sudo apt-get install -y -f
$ sudo rm google-chrome-stable_current_amd64.deb
```

### Chromedriver install

```
$ latest_version=$(wget https://chromedriver.storage.googleapis.com/LATEST_RELEASE -O -)
$ wget https://chromedriver.storage.googleapis.com/${latest_version}/chromedriver_linux64.zip
$ unzip chromedriver_linux64
$ mv chromedriver webstaBot/assets/chromedriver
$ chmod +x webstaBot/assets/chromedriver
$ chmod 755 webstaBot/assets/chromedriver
$ cd webstaBot
``` 

### Make sure you also have the latest version of urllib3

```
$ cd ~
$ sudo pip install urllib3 --upgrade
```


Replace the information in webstabot.py listed below with your own.

KEYWORDS = ["modernart","artgallery","model","contemporaryart","oshitwaddup"] # Tags to follow

MY_USER = 'USERNAME' # Replace with your username

MY_PASSWORD = 'PASSWORD' # Replace with your password

Then run "python webstabot.py" and that's it!


