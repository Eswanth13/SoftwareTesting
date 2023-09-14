#locaters
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.google.com/gmail/about/")
#links=driver.find_element(By.CSS_SELECTOR,".button").click()
# driver.find_element(By.CSS_SELECTOR,"a[data-action=sign in]").click()
driver.find_element(By.XPATH,"/html/body/header/div/div/div/a[2]").click()
driver.find_element(By.XPATH,"//*[@id='identifierId']").send_keys("eswanth1304@gmail.com")
driver.find_element(By.XPATH,"//*[@id='identifierNext']/div/button/span").click()




sleep(10)