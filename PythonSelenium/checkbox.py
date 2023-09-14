
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.techlistic.com/p/selenium-practice-form.html#google_vignette")
driver.maximize_window()

#select specific checkbox
#check=driver.find_element(By.XPATH,"//input[@id='tool-0']").click()#tag & id
#driver.find_element(By.XPATH,"//*[@id='tool-0']").click()#relative xpath
check=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'tool')]")
print(len(check))

#select multiple checkbox by choice
# for i in check:
#     toolname=i.get_attribute("id")
#     if toolname=="tool-0" or toolname=="tool-2":
#         i.click()
#select last 2 checkbox
# for i in range(len(check)-2,len(check)):
#     check[i].click()

#select first 2 checkbox
# for i in range(len(check)):
#     if i<2:
#         check[i].click()

#clear all the check boxes
# for i in check:
#     if i.is_selected():
#         i.click()

sleep(8)