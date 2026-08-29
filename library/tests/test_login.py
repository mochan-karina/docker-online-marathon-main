import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_and_logout():
    driver = webdriver.Chrome()

    try:
        driver.get("http://127.0.0.1:8000/auth/")
        time.sleep(2)

        email = driver.find_element(
            By.CSS_SELECTOR,
            "input[name='email']",
        )
        password = driver.find_element(
            By.CSS_SELECTOR,
            "input[name='password']",
        )

        email.send_keys("karina@gmail.com")
        time.sleep(1)

        password.send_keys("08082007")
        time.sleep(1)

        login_button = driver.find_element(
            By.CSS_SELECTOR,
            "button[type='submit']",
        )
        login_button.click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be("http://127.0.0.1:8000/book/")
        )
        time.sleep(3)

        assert driver.current_url == "http://127.0.0.1:8000/book/"

        logout_button = driver.find_element(
            By.CSS_SELECTOR,
            "form[action='/auth/logout/'] button",
        )
        time.sleep(2)
        logout_button.click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be("http://127.0.0.1:8000/auth/")
        )
        time.sleep(3)

        assert driver.current_url == "http://127.0.0.1:8000/auth/"

        email = driver.find_element(
            By.CSS_SELECTOR,
            "input[name='email']",
        )
        password = driver.find_element(
            By.CSS_SELECTOR,
            "input[name='password']",
        )

        email.send_keys("karina@gmail.com")
        time.sleep(1)

        password.send_keys("wrong_password")
        time.sleep(1)

        login_button = driver.find_element(
            By.CSS_SELECTOR,
            "button[type='submit']",
        )
        login_button.click()

        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "p")
            )
        )
        time.sleep(3)

        assert error_message.text == "Invalid email or password"
        assert driver.current_url == "http://127.0.0.1:8000/auth/"

    finally:
        driver.quit()