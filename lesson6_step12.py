from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector('.form-group :nth-child(2)')
    robots_checked = x_element.get_attribute('valuex')
    x = robots_checked
    y = calc(x)

    input3 = browser.find_element_by_css_selector('#answer')
    input3.send_keys(y)

    option1 = browser.find_element_by_css_selector('#robotCheckbox')
    option1.click()

    option2 = browser.find_element_by_css_selector("#robotsRule")
    option2.click()

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