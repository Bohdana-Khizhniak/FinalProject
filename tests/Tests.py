from time import sleep
# import allure
from selene import have, command
from selene.support.shared import browser
from sinsay_testing.Model import Sin

# @allure.title('Тест для перевірки головної сторінки')
def test_main_page():
    # with allure.step('Відкриваємо сайт Sinsay'):
    Sin.open()
    assert Sin.should_be('https://www.sinsay.com/ua/uk/')
def test_authorization():
    # with allure.step('Відкриваємо сторінку авторизації'):
    Sin.authorization('dana24146@gmail.com', 'dana310785')
    assert Sin.should_be('Богдана')
def test_serch():
    # with allure.step('Перевірка пошуку'):
    Sin.serch('сумка')
    assert Sin.should_be('сумка')
def test_basket():
    # with allure.step('Перевірка кошику'):
    Sin.basket()
    assert Sin.should_be('сумка')
def test_data_change():
    Sin.data_change()