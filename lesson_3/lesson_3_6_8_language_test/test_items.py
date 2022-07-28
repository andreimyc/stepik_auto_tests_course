import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_element(By.CSS_SELECTOR, "[class='btn btn-lg btn-primary btn-add-to-basket']")
    assert button == browser.find_element(By.CSS_SELECTOR, "[class='btn btn-lg btn-primary btn-add-to-basket']")
