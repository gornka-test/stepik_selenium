from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    input3 = browser.find_element_by_css_selector('.form-control')
    input3.send_keys(y)

    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()

    option1 = browser.find_element_by_css_selector("#robotsRule")
    option1.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn")
    button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()