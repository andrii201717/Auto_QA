from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import time

# Опції браузера
options = Options()
# options.add_argument("--headless")  # Убери комментарий, если хочешь в фоновом режиме

# Старт драйвера
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

try:
    # Открыть сайт
    driver.get("https://itcareerhub.de/ru")
    time.sleep(5)  # Ждём полной загрузки

    # Клик по ссылке "Способы оплаты"
    link = driver.find_element(By.LINK_TEXT, "Способы оплаты")
    link.click()
    time.sleep(3)

    # Найдём заголовок раздела или текст
    heading = driver.find_element(By.XPATH, "//*[contains(text(), 'Способы оплаты')]")

    # Скроллим к нему
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", heading)
    time.sleep(2)

    # Делаем скриншот всей видимой части (или страницы)
    driver.save_screenshot("payment_section_visible.png")
    print("Скриншот сохранён как 'payment_section_visible.png'.")

finally:
    driver.quit()
