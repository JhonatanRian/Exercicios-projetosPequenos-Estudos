from time import sleep
from selenium import webdriver

user = input("")

with webdriver.Firefox() as driver:
    while True:
        var = None
        driver.get("https://www.bet365.com/#/HO/")
        sleep(3)
        elem = driver.find_elements_by_tag_name("div")
        for el in elem:
            if el.text == "Login":
                var = el
                break
        var.click()
        ele = driver.find_elements_by_tag_name("input")
        for el in ele:
            if el.get_attribute("placeholder") == "Usuário":
                var = el
                el.send_keys(user)
            if el.get_attribute("placeholder") == "Senha":
                el.send_keys(password)
                break
    
    sleep(2)
