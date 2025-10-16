from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.headless = False
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)

driver.get('https://transcripts.foreverdreaming.org/viewforum.php?f=177')
links = driver.find_elements(by=By.CLASS_NAME, value="topictitle")
f = open("script.txt", "a")

for link in links:
    try:
        driver = webdriver.Chrome(service=Service(
            ChromeDriverManager().install()), options=options)
        driver.get(link.get_attribute('href'))
        time.sleep(2)
        element = driver.find_element(
            By.XPATH, '/html/body/div[2]/div[2]/div[3]/div[1]/div[2]/div/div/div/div[2]')
        f.write(element.text)

        # element = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/div[1]/p/a[5]')
        # element.click()
    except Exception as e:
        print(e)
        print('ufkedup')

f.close()

# from twython import Twython
# import json

# with open("twitter_credentials.json", "r") as file:
#     creds = json.load(file)

# CONSUMER_KEY = creds["CONSUMER_KEY"]
# CONSUMER_SECRET = creds["CONSUMER_SECRET"]
# ACCESS_KEY = creds["ACCESS_TOKEN"]
# ACCESS_SECRET = creds["ACCESS_SECRET"]

# # Authenticate to Twitter
# twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

# photo = open('jus-reign-there.gif', 'rb')
# response = twitter.upload_media(media=photo)
# twitter.update_status(status='come back my man',
#                       media_ids=[response['media_id']])
