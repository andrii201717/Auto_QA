from selenium import webdriver
from selenium.webdriver.common.by import By

def test_find_text_in_iframe():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
    driver.maximize_window()

    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    target_text = "semper posuere integer et senectus justo curabitur."
    text_found = False

    for iframe in iframes:
        driver.switch_to.default_content()
        driver.switch_to.frame(iframe)

        paragraphs = driver.find_elements(By.TAG_NAME, "p")
        for p in paragraphs:
            if target_text in p.text:
                text_found = True
                break

        if text_found:
            break

    driver.quit()
    assert text_found, "Текст не знайдено в жодному iframe."
