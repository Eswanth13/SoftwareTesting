from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()



driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.ID,'openwindow').click()
windowid=driver.window_handles

parentwindowid=windowid[0]
childwindowid=windowid[1]

print(parentwindowid, childwindowid)

# driver.switch_to.window(childwindowid)
# print(driver.title)
# driver.switch_to.window(parentwindowid)
# print(driver.title)

            #or

for drive in windowid :
    driver.switch_to.window(drive)
    print(driver.title)


# if we need to close a particular window

for drive in windowid :
    driver.switch_to.window(drive)
    if driver.title=="Practice Page":
        driver.close()

sleep(3)

