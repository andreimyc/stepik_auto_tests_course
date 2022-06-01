from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполнить текстовое поле Имя
    input1 = browser.find_element_by_css_selector("[name='firstname']")
    input1.send_keys("Andrei")
    
    # Заполнить текстовое поле Фамилия
    input1 = browser.find_element_by_css_selector("[name='lastname']")
    input1.send_keys("Myc")
    
    # Заполнить текстовое поле Email
    input1 = browser.find_element_by_css_selector("[name='email']")
    input1.send_keys("andrei@mail.ru")
    
    # Загрузка файла .txt
    import os
    current_dir = os.path.abspath(os.path.dirname('__file__'))  
    file_path = os.path.join(current_dir, 'file.txt')  
    element = browser.find_element_by_name("file")
    element.send_keys(file_path)   
        
    # Нажать на кнопку Submit
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()    
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)    
    # закрываем браузер после всех манипуляций
    browser.quit()