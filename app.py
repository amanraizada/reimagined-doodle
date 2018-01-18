from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time,sys,requests,threading
print("STARTING")

url = requests.get("http://textuploader.com/dmchc/raw")
urls = url.text

urls = urls.split("\n")


chrome_options = Options()  
chrome_options.binary_location = r"/app/.apt/usr/bin/google-chrome"
            
driver = webdriver.Chrome(chrome_options=chrome_options)
# driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=chrome_options)

while True:
    for i in urls:
        while True:
            try:
                print(">> OPENING : " + i[:30])
                driver.get(i)
                print(">> SUCCESS")
                # driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL +"t")
                time.sleep(1)
                break
            except:
                print(">> ERROR WHILE : " + i[:30])
                continue
    print(">> SLEEPING 60 SECONDS")
    time.sleep(60)
