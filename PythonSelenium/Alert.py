from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.find_element(By.ID,'alertbtn').click()
# driver.switch_to.alert.accept()

# driver.find_element(By.ID,'confirmbtn').click()
# driver.switch_to.alert.dismiss()
driver.find_element(By.NAME,'enter-name').send_keys('yesh')

driver.find_element(By.ID,'confirmbtn').click()
print(driver.switch_to.alert.text)
sleep(3)

