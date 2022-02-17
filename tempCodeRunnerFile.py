    email = browser.find_element_by_id("UserID")
    email.send_keys(username)

    passW = browser.find_element_by_id("PIN")
    passW.send_keys(password)

    Login = browser.find_element_by_xpath("/html/body/div[3]/form/p/input")
    Login.click()

    Stud = browser.find_element_by_xpath("/html/body/div[3]/table[1]/tbody/tr[3]/td[2]/a")
    Stud.click()

    Reg = browser.find_element_by_xpath("/html/body/div[3]/table[1]/tbody/tr[1]/td[2]/a")
    Reg.click()


    Add = browser.find_element_by_xpath("/html/body/div[3]/table[1]/tbody/tr[2]/td[2]/a")
    Add.click()

    time.sleep(8) #wait 8 seconds for exit
    err = browser.find_element_by_xpath("/html/body/div[3]/form/table/tbody/tr/td[2]/span")
    if(err):
        print("Error occured!!! No Terms Available")
        exitButton = browser.find_element_by_xpath("/html/body/div[1]/table/tbody/tr/td[2]/p/span/a[2]")
        exitButton.click()
        hmPg = browser.find_element_by_xpath("/html/body/div[3]/a[2]")
        hmPg.click()
