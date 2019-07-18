from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
    """Посчитать математическую функцию от x (код для этого приведён ниже)."""
    return str(math.log(abs(12*math.sin(int(x)))))


#Открыть страницу http://suninjuly.github.io/explicit_wait2.html.
browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")


# # ждем загрузки страницы
# time.sleep(2)


# #Нажать на кнопку Забронировать.
# button = browser.find_element_by_css_selector("button.btn")
# button.click()


# находим элемент, содержащий текст
text_element = browser.find_element_by_xpath('//*[@id="price"]')


print(text_element.text)
# говорим WebDriver искать каждый элемент в течение 5 секунд
# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.XPATH, '//*[@id="price"]'), "10000 RUR")
    )
#Нажать на кнопку Забронировать.
button = browser.find_element_by_css_selector("button.btn")
button.click()


#Считать значение для переменной x.
x_element = browser.find_element_by_css_selector("span#input_value")
print("span#input_value: ", x_element)
x = x_element.text
print("Икс: ", x)
y = calc(x)

#Ввести ответ в текстовое поле.
input1 = browser.find_element_by_id("answer")
input1.send_keys(calc(x))


#Нажать на кнопку Отправить.
button = browser.find_element_by_id("solve")
button.click()
