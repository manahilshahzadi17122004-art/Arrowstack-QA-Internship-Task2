from selenium.webdriver.common.by import By

BASE_URL = "https://www.saucedemo.com"


def login(driver, username, password):
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()


def get_error_text(driver):
    return driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text


def test_valid_login(driver):
    login(driver, "standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url


def test_wrong_password(driver):
    login(driver, "standard_user", "wrong123")
    assert "do not match" in get_error_text(driver)


def test_empty_username(driver):
    login(driver, "", "secret_sauce")
    assert "Username is required" in get_error_text(driver)


def test_empty_password(driver):
    login(driver, "standard_user", "")
    assert "Password is required" in get_error_text(driver)


def test_locked_out_user(driver):
    login(driver, "locked_out_user", "secret_sauce")
    assert "locked out" in get_error_text(driver)