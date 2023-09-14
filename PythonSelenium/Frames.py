#HTML frames used to divide a web page into separate sections, each with its own HTML document.

#Frames/Iframes
#selenium4
#switch_to.frame(name of the frame)
#switch_to.frame(id of the frame)
#switch_to.frame (webelement)
#switch_to.frame(0)

#switch_to.default_content()
#switch_to.parent_frame()


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

try:
    driver.switch_to.frame("iframe-name")
    sleep(2)
    driver.find_element(By.XPATH,"//a[text()='Login']").click()
except NoSuchElementException:
    print('Might be inside iframe')

# if driver.switch_to.alert.text.__contains__('sdlkjs'):
#     print('Test case Pass')
# else:
#     print('Test case Failed')
driver.switch_to.default_content()# Go Back To Main page

alertMessage = 'Testing'
driver.find_element(By.NAME,'enter-name').send_keys(alertMessage)
driver.find_element(By.ID,'confirmbtn').click();
sleep(2)
#driver.switch_to.alert.dismiss()
print(driver.switch_to.alert.text)

sleep(5)