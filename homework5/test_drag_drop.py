from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_drag_and_drop_image():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")

    wait = WebDriverWait(driver, 10)

    # iframe містить drag&drop функціонал — спочатку перемикаємось у нього
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe.demo-frame")))

    # Знаходимо всі зображення в галереї
    images = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#gallery > li")))
    assert len(images) == 4, "Очікується 4 зображення в початковій галереї"

    first_image = images[0]

    # Знаходимо елемент корзини
    trash = wait.until(EC.presence_of_element_located((By.ID, "trash")))

    # Виконуємо drag and drop
    ActionChains(driver).drag_and_drop(first_image, trash).perform()

    # Трохи чекаємо після дії
    time.sleep(1)

    # Перевіряємо, що в Trash додалась 1 картинка
    trashed_items = driver.find_elements(By.CSS_SELECTOR, "#trash > ul > li")
    assert len(trashed_items) == 1, "Очікується 1 зображення в корзині після переміщення"

    # І залишилось 3 картинки у вихідній галереї
    remaining_items = driver.find_elements(By.CSS_SELECTOR, "#gallery > li")
    assert len(remaining_items) == 3, "Очікується 3 зображення в галереї після переміщення"

    driver.quit()
