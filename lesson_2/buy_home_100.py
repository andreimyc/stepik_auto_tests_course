from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Дождаться, когда цена дома уменьшится до 100
    WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button = browser.find_element_by_css_selector("#book")
    button.click()
       
    # Посчитать математическую функцию от x (код для этого приведён ниже)
    import math
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    
    # Считать значение для переменной x
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    
    # Ввести ответ в текстовое поле
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
    
    # Нажать на кнопку Submit
    button = browser.find_element_by_css_selector("#solve")
    button.click()    
    
    # Вывести ответ с модального окна
    alert = browser.switch_to.alert
    answer = alert.text.split()[-1]
    print(answer) 
       
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)    
    # закрываем браузер после всех манипуляций
    browser.quit()