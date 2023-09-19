# xpath
# --XPath is defined as XML path.
# --It is a syntax or language for finding any element on the web page using XML path expression.
# --XPath is used to find the location of any element on a webpage using HTML DOMI structure.
# --XPath can be used to navigate through elements and attributes in DOM.
# --XPath is an address of the element.


#create own xpath
# eg:Xpath,"//tagname[@attribute='value']"
# Xpath,"//input[@type='text']"
# Xpath,"//label[@id='message23']"
# Xpath,"//input[@value='RESET']"
# Xpath,"//*[@class='barone']"
# Xpath,"//a[@href='http://demo.guru99.com/']"
# Xpath,"//img[@src='//guru99.com/images/home/java.png']"

#------this is not a xpath
# driver.find_element(By.ID,"username").send_keys("student")
# driver.find_element(By.NAME,"password").send_keys("Password123")
# driver.find_element(By.ID,"submit").click()
#
#using AND & OR
# Xpath=//*[@type='submit' or @name='btnReset']
#Xpath=//input[@type='submit' and @name='btnLogin']
#
#using Contains()
#Xpath=//*[contains(@type,'sub')]
#Xpath=//*[contains(@name,'btn')]






from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
#full xpath
driver.find_element(By.XPATH,"/html/body/div/div/section/section/div[1]/div[1]/input").send_keys("student")
#relative xpath
driver.find_element(By.XPATH,"//*[@id='password']").send_keys("Password123")

