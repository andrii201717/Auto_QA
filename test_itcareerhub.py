import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_logo(driver):
    driver.get("https://itcareerhub.de/ru")
    element = driver.find_element(By.CLASS_NAME, "tn-elem__7178437221710153310155")
    assert element, "тест не прошел"

def test_programs(driver):
    driver.get("https://itcareerhub.de/ru")
    element = driver.find_element(By.LINK_TEXT, 'Программы')
    assert element, "тест не прошел"

def test_payment(driver):
    driver.get("https://itcareerhub.de/ru")
    element = driver.find_element(By.LINK_TEXT, 'Способы оплаты')
    assert element, "тест не прошел"

def test_news(driver):
    driver.get("https://itcareerhub.de/ru")
    element = driver.find_element(By.LINK_TEXT, 'Новости')
    assert element, "тест не прошел"

def test_about_us(driver):
    driver.get("https://itcareerhub.de/ru")
    element = driver.find_element(By.LINK_TEXT, 'О нас')
    assert element, "тест не прошел"

def test_reviews(driver):
    driver.get("https://itcareerhub.de/ru")
    element = driver.find_element(By.LINK_TEXT, 'Отзывы')
    assert element, "тест не прошел"

def test_de(driver):
    driver.get("https://itcareerhub.de/ru")
    element = driver.find_element(By.LINK_TEXT, 'de')
    assert element, "тест не прошел"

def test_ru(driver):
    driver.get("https://itcareerhub.de/ru")
    element = driver.find_element(By.LINK_TEXT, 'ru')
    assert element, "тест не прошел"

def test_call(driver):
    driver.get("https://itcareerhub.de/ru")
    element = driver.find_element(By.CLASS_NAME, "tn-elem__7178437221710153310161")

    assert element, "Элемент трубка не найден"

    element.click()
    time.sleep(1)
    element1 = driver.find_element(By.XPATH, '//*[text()="Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами"]')

    assert element1, "Элемент 'Если не дозвонились - не найден'"