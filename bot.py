#developed by Alper Kaan Odabasoglu at 17.02.2022

"""
Aim of this project is to access the add drop page of Sabancı University to select Courses for next semester.
Automation with selenium is used to navigate between pages and access to the intended page
Don't feel under pressure anymore and use this software to avoid from stress. Have Fun :)
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


username = "kaanalper"
password = "Alpero2001"

CrnArr = [20222,
            20225,
            20227,
            20228, 
            20594, 
            20602, 
            21036, 
            21051, 
            21060, 
            21064
        ]

driver = webdriver.Chrome()
driver.get(('https://suis.sabanciuniv.edu/prod/twbkwbis.P_SabanciLogin'))

URL = "https://suis.sabanciuniv.edu/prod/twbkwbis.P_GenMenu?name=bmenu.P_MainMnu"

#"https://suis.sabanciuniv.edu/prod/bwskfreg.P_AltPin"   "https://suis.sabanciuniv.edu/prod/twbkwbis.P_GenMenu?name=bmenu.P_MainMnu"

while(driver.current_url != URL):

    email = driver.find_element_by_id("UserID")
    email.send_keys(username)

    passW = driver.find_element_by_id("PIN")
    passW.send_keys(password)
    
    Login = driver.find_element_by_xpath("/html/body/div[3]/form/p/input")
    Login.click()

    if(driver.current_url != URL):
        driver.get(('https://suis.sabanciuniv.edu/prod/twbkwbis.P_SabanciLogin'))


"""
Stud = driver.find_element_by_xpath("/html/body/div[3]/table[1]/tbody/tr[3]/td[2]/a")
Stud.click()

Reg = driver.find_element_by_xpath("/html/body/div[3]/table[1]/tbody/tr[1]/td[2]/a")
Reg.click()


Add = driver.find_element_by_xpath("/html/body/div[3]/table[1]/tbody/tr[2]/td[2]/a")
Add.click()

time.sleep(1) #wait 8 seconds for exit
err = driver.find_element_by_xpath("/html/body/div[3]/form/table/tbody/tr/td[2]/span")
if(err):
    print("Error occured!!! No Terms Available")
    exitButton = driver.find_element_by_xpath("/html/body/div[1]/table/tbody/tr/td[2]/p/span/a[2]")
    exitButton.click()
    hmPg = driver.find_element_by_xpath("/html/body/div[3]/a[2]")
    hmPg.click()
    
"""