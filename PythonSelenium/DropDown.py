from selenium import webdriver
from selenium.common import WebDriverException, NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.implicitly_wait(5)

url = 'https://rahulshettyacademy.com/AutomationPractice/'
#url = "https://www.globalsqa.com/demo-site/select-dropdown-menu/"

driver.get(url)
#a=driver.find_elements(By.XPATH,"//select[@fdprocessedid='sfdrui']")

# try:
#     dropcountry=Select(driver.find_element(By.XPATH,"//div[@class='information closable']/following-sibling::p/select"))
#     dropcountry.select_by_value("IND");
#
#     alloptions=dropcountry.options
#     flag = False
#     for a in alloptions:
#         if a.text=='Indai':
#             flag = True
#             break
#
#     dropcountry.select_by_index(len(alloptions)-1);
#
#     if flag:
#         print("Test Case pass - Dropdown has Option 'India'")
#     else:
#         print("Test Case fail - Dropdown hasnt got the option 'India'")
# except NoSuchElementException:
#     print("Kindly check the xpath of the select webelement")

#driver.find_element(By.ID,'alertbtn').click();
#driver.switch_to.alert.accept()
alertMessage = 'Testing'
driver.find_element(By.NAME,'enter-name').send_keys(alertMessage)
driver.find_element(By.ID,'confirmbtn').click();
sleep(2)
#driver.switch_to.alert.dismiss()
print(driver.switch_to.alert.text)

if driver.switch_to.alert.text.__contains__('sdlkjs'):
    print('Test case Pass')
else:
    print('Test case Failed')

#driver.find_element(By.LINK_TEXT,"Home").click()
sleep(5)