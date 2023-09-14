from time import sleep

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
#driver.implicitly_wait(6)
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()
allLinks=driver.find_elements(By.TAG_NAME,"a")
count=0


for links in allLinks:
    url=links.get_attribute('href')
    try:
        res=requests.head(url)
    except:
        None

    if res.status_code>=400:
        print(url,"is broken links")
        count=count+1
    else:
        print(url,"valid links")

print(count)

driver.quit()
