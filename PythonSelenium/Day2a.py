# CSS Selectors
#
# 1) tag id -------------tagname#valueofId  or  input#email
# 2) tag class-----------tagname.valueofClass input.inputtext_55r1 61uy
# 3) tag attribute-------tagname [attribute=value]  eg:input[data-testid-royal_email]
# 4) tag class attribute--tagname.valueofClass [attribute-value] eg: input.inputtext [data-testid=royal_pass]


from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login//")
#tag id
#driver.find_element(By.CSS_SELECTOR,"input#username").send_keys("student")
driver.find_element(By.CSS_SELECTOR,"#username").send_keys("student")
driver.find_element(By.CSS_SELECTOR,"#password").send_keys("Password123")
#tag class
driver.find_element(By.CSS_SELECTOR,".btn").click()



sleep(10)