from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    import math
    
    # Посчитать математическую функцию от x (код для этого приведён ниже)
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    
    # Считать значение для переменной x
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    
    # Проскролить страницу вниз
    button = browser.execute_script("window.scrollBy(0, 150);")
           
    # Ввести ответ в текстовое поле
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
    
    # Отметить checkbox "I'm the robot"
    option1 = browser.find_element_by_css_selector("#robotCheckbox")
    option1.click()    
    
    # Выбрать radiobutton "Robots rule!"
    option2 = browser.find_element_by_css_selector("#robotsRule")
    option2.click()     
    
    # Нажать на кнопку Submit
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()    
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)    
    # закрываем браузер после всех манипуляций
    browser.quit()