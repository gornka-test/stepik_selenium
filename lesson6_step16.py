from selenium import webdriver
import time
import os
import math

def calc(a):
    return str(math.log(abs(12 * math.sin(a))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_css_selector('.btn-primary')
    button1.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    a = browser.find_element_by_css_selector('#input_value')
    x = int(a.text)
    x = calc(x)

    input1 = browser.find_element_by_css_selector('#answer')
    input1.send_keys(x)

    button2 = browser.find_element_by_css_selector('.btn-primary')
    button2.click()

# ждем загрузки страницы
    time.sleep(10)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()