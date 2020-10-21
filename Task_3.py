from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def login(username, password):
    browser = webdriver.Chrome('path_to_chromedriver')

    browser.get('https://passport.yandex.ru/auth/list')

    username_input = browser.find_element_by_name('login')
    username_input.clear()
    username_input.send_keys(username)
    username_input.send_keys(Keys.ENTER)

    time.sleep(2)

    password_input = browser.find_element_by_name('passwd')
    password_input.clear()
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)

    time.sleep(2)

    try:
        error = browser.find_element_by_class_name("Textinput-Hint")
    except Exception as ex:
        error = False
        print(ex)

    browser.close()
    browser.quit()

    if error:
        return False
    else:
        return True
