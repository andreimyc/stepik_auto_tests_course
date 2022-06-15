from selenium import webdriver
import time
import unittest

def link_t(link):
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector("[placeholder='Input your first name']").send_keys("Ivan")
    browser.find_element_by_css_selector("[placeholder='Input your last name']").send_keys("Ivanov")
    browser.find_element_by_css_selector("[placeholder='Input your email']").send_keys("ivan@mail.ru")
    browser.find_element_by_css_selector("button.btn").click()

    time.sleep(1)
    return browser.find_element_by_tag_name("h1").text


class tast_reg1(unittest.TestCase):
    def test_reg1(self):
        self.assertEqual(link_t("http://suninjuly.github.io/registration1.html"),
                         "Congratulations! You have successfully registered!", "registration is failed")


    def test_reg2(self):
        self.assertEqual(link_t("http://suninjuly.github.io/registration2.html"),
                         "Congratulations! You have successfully registered!", "registration is failed")

if __name__ == "__main__":
    unittest.main()