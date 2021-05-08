from selenium import webdriver
import time
import os
import math

def calc(a):
    return str(math.log(abs(12 * math.sin(a))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_css_selector('.btn-primary')
    button1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)


    a = browser.find_element_by_css_selector('#input_value')
    x = int(a.text)
    x = calc(x)

    input1 = browser.find_element_by_css_selector('#answer')
    input1.send_keys(x)

    button1 = browser.find_element_by_css_selector('.btn-primary')
    button1.click()

# ждем загрузки страницы
    time.sleep(10)



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(50)
    # закрываем браузер после всех манипуляций
