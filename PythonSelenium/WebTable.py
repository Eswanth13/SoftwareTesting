#1) Count number of rows & columns
#2) Read specifid row & Column data
#3) Read all the rows & Columns data
#4)Read Data based on condition(List  Price 25 with name



from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#1) Count number of rows & columns
nocolumn=len(driver.find_elements(By.XPATH,"//table[@NAME='courses']/tbody/tr[1]/th"))
norows=len(driver.find_elements(By.XPATH,"//table[@NAME='courses']/tbody/tr"))
print(norows)#11
print(nocolumn)#3

#2) Read specifid row & Column data
d=driver.find_element(By.XPATH,"//table[@NAME='courses']/tbody/tr[6]/td[2]").text
print(d)

#3) Read all the rows & Columns data

for r in range(2,norows+1):
    for c in range(1,nocolumn+1):
        data=driver.find_element(By.XPATH,"//table[@NAME='courses']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(data,end="      ")
    print()

#4)Read Data based on condition(List  Price 25 with name
for r in range(2,norows+1):
    instprice=driver.find_element(By.XPATH,"//table[@NAME='courses']/tbody/tr["+str(r)+"]/td[3]").text
    if instprice=="20":
        instname=driver.find_element(By.XPATH,"//table[@NAME='courses']/tbody/tr["+str(r)+"]/td[1]").text
        instcourse = driver.find_element(By.XPATH, "//table[@NAME='courses']/tbody/tr[" + str(r) + "]/td[2]").text
        instprice = driver.find_element(By.XPATH, "//table[@NAME='courses']/tbody/tr[" + str(r) + "]/td[3]").text

        print(instname,instcourse,instprice)
