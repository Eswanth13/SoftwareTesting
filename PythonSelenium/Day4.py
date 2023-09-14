from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


options = Options()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()

driver.get("https://practicetestautomation.com/practice-test-login/")
driver.find_element(By.ID,"username").send_keys("student")
driver.find_element(By.NAME,"password").send_keys("Password123")
driver.find_element(By.ID,"submit").click()
driver.find_element(By.XPATH,"//*[@id='menu-item-43']/a").click()
driver.find_element(By.XPATH,"//*[@id='loop-container']/div/article/div[2]/p[14]/a/strong").click()

links=driver.find_elements(By.TAG_NAME,"a")
print(len(links))
#driver.close() #--close single browser windows(where driver focused
#driver.quit()  #---close multiple browser windows(this will kill the process)
#sleep(10)