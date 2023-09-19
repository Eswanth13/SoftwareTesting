from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.globalsqa.com/demo-site/datepicker/#Icon%20Trigger")

#frame
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame lazyloaded']"))
#driver.find_element(By.XPATH,"//*[@id='datepicker']").send_keys("04/13/2023")#mm/dd/yyyy

driver.find_element(By.ID,"datepicker").click()#opens datepicker
mm="March"
yy="2025"
dd="13"

while True:
    month=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    year=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if month==mm and year==yy:
        break
    else:
        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()#use for future dates
        #driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']").click()#use for past dates eg:(dob)

#select date
date=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for ele in date:
    if ele.text==dd:
        ele.click()
        break
sleep(3)