from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time,sys,requests,threading
print("STARTING")
def OpenWeb(u):
    print(u)
    chrome_options = Options()  
    chrome_options.binary_location = r"/app/.apt/usr/bin/google-chrome"
    driver = webdriver.Chrome(chrome_options=chrome_options)
    # driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=chrome_options)
    while True:
        try:
            driver.get(u)
            time.sleep(60)
            print("Refreshing " + u)
        except:
            continue
        

url = requests.get("http://textuploader.com/dmchc/raw")
urls = url.text

urls = urls.split("\n")

for i in urls:
    while True:
        try:
            thread = threading.Thread(target=OpenWeb, args=([i]))
            thread.start()
            time.sleep(10)
            break
        except:
            continue

