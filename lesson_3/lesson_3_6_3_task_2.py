import pytest
import time
import math
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    # ожидание прогрузки страницы
    browser.implicitly_wait(20)
    yield browser
    print("\nquit browser..")
    browser.quit()


# в качестве аргументов передаётся изменяемая часть ссылок
@pytest.mark.parametrize('module', ['236895', '236896', '236897', '236898',
                                    '236899', '236903', '236904', '236905'])
def test_links(browser, module):
    answer = math.log(int(time.time()))
    browser.get(f'https://stepik.org/lesson/{module}/step/1')
    browser.find_element_by_css_selector('textarea').send_keys(str(answer))
    browser.find_element_by_class_name('submit-submission').click()
    result = browser.find_element_by_class_name('smart-hints__hint').text
    assert result == 'Correct!', 'message is not "Correct!"'