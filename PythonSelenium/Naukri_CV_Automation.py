import time
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.naukri.com/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.ID,"login_Layer").click()
#driver.find_element(By.XPATH,"//input[@class='err-border']").send_keys("eswanth1304@gmail.com")----
driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div/div/div[2]/div/form/div[2]/input").send_keys("eswanth1304@gmail.com")
#driver.find_element(By.XPATH,"//input[@class='err-border']").send_keys("eswanth1304@gmail.com")-----
#driver.execute_script("document.getElementByClass('err-border').value = 'eswanth1304@gmail.com'")----
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("Redred10@")
driver.find_element(By.XPATH,"//button[@class='btn-primary loginButton']").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Complete").click()
driver.find_element(By.ID,"attachCV").send_keys("C://eswanth_cv/Eswanth_cv.pdf")
dd=driver.find_element(By.XPATH,"//div[@class='updateOn typ-14Regular']").text
print(dd)
time.sleep(3)

td=date.today()
currentdate=td.strftime("Uploaded on %b %d, %Y")
#cd=f"Uploaded on {currentdate}"
print(currentdate)
if currentdate==dd:
    print("Resume is updated successfully")
else:
    print("Resume is not Updated")

