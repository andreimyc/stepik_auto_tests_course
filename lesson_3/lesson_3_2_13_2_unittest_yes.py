import unittest
import time
from selenium import webdriver

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        #link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector("[placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("[placeholder='Input your last name']")
        input2.send_keys("Ivanov")
        input3 = browser.find_element_by_css_selector("[placeholder='Input your email']")
        input3.send_keys("ivan@mail.ru")


        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        #assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
        # self.assertEqual('что должно быть', 'что есть', 'что произошло')
        self.assertEqual(welcome_text, welcome_text_elt.text, "Поздравляем! Вы успешно зарегистировались!")
        
    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector("[placeholder='Input your name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("[placeholder='Input your email']")
        input2.send_keys("ivan@mail.ru")


        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        #assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
        # self.assertEqual('что должно быть', 'что есть', 'что произошло')
        self.assertEqual(welcome_text, welcome_text_elt.text, "Поздравляем! Вы успешно зарегистировались!")
        
if __name__ == "__main__":
    unittest.main()