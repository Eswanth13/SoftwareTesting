#--------

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.globalsqa.com/demo-site/datepicker/#Icon%20Trigger")
#driver.get_screenshot_as_file("C:\\Users\\eswan\\OneDrive\\Desktop\\HomePage.png")

element = driver.find_element(By.ID,'DropDown DatePicker')
element1 = driver.find_element(By.LINK_TEXT,'Home')
element2 = driver.find_element(By.PARTIAL_LINK_TEXT,'GlobalSQA')

driver.execute_script("arguments[0].scrollIntoView();", element1)
driver.execute_script("arguments[0].scrollIntoView();", element2)
driver.execute_script("arguments[0].click();",element)
#driver.get_screenshot_as_file("C:\\Users\\eswan\\OneDrive\\Desktop\\Screenshot.png")


driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame lazyloaded']"))
#driver.execute_script("arguments[0].click();",driver.find_element(By.XPATH,"//*[@id='datepicker']").click())
driver.execute_script("arguments[0].click();",driver.find_element(By.ID,'datepicker'))
#driver.find_element(By.CLASS,"hasDatepicker").click()

driver.execute_script("document.getElementById('datepicker').value = '20/15/2022'")


sleep(3)