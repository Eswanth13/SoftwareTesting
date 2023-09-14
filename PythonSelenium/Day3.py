#------------applicationCmd-------
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")#get commend
# print(f"{driver.title} title page")#title commend
# print(f"{driver.current_url} current url")#current url commend
# print(driver.page_source)#page sourse commend
#case1=give username
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("rahulshettyacademy")
#case2=give password
driver.find_element(By.XPATH,"//input[@class='form-control' and @id='password']").send_keys("learning")
#case3=select radio button
driver.find_element(By.XPATH,"//input[@value='admin' and @checked='checked']").click()
#case4=select option
driver.find_element(By.XPATH,"//option[@value='teach']").click()
#case5=click check box
#driver.find_element(By.XPATH,"//input[@id='terms']").click()
driver.find_element(By.XPATH,"//input[contains(@type,'check')]").click()#using contains(don't need to write a full value) xpath
#case6=click signin
driver.find_element(By.XPATH,"//input[contains(@class,'btn') and contains(@name,'sign')]").click()

#case7=click home
#driver.find_element(By.XPATH,"//a[@href='/angularpractice']").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Home").click()
#driver.find_element(By.XPATH,"//input[@minlength='2']").send_keys("eswanth")

links=driver.find_elements(By.TAG_NAME,"a")
print(len(links))

sleep(8)