from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажать на кнопку
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()
    
    # Переключение на новую вкладку
    browser.switch_to.window(browser.window_handles[1])
          
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
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()    
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)    
    # закрываем браузер после всех манипуляций
    browser.quit()