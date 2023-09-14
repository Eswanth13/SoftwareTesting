#1) Open Web Browser (Chrome/firefox/Edge).
#2) Open URL https://opensource-demo.orangehrmlive.com/
#3) Enter username (Admin).
#4) Enter password (admin123).
#5) Click on Login.
#6) Capture title of the home page. (Actual title)
#7) Verify title of the page: OrangeHRM (Expected)
#8) close browser

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.NAME,"username").send_keys("rahulshettyacademy")
driver.find_element(By.NAME,"password").send_keys("learning")
driver.find_element(By.NAME,"signin").click()

act_title=driver.title
exp_title='LoginPage Practise | Rahul Shetty Academy'

if act_title==exp_title:
    print("login test success")
else:
    print("Login Test Fail")

#driver.maximize_window()
#sleep(10)
#driver.close()
