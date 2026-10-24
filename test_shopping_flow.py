from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com"


def login(driver):
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()


def add_backpack(driver):
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()


def open_cart(driver):
    driver.find_element(By.CSS_SELECTOR, "[data-test='shopping-cart-link']").click()


def cart_item_names(driver):
    items = driver.find_elements(By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    return [item.text for item in items]


def test_add_item_updates_cart_badge(driver):
    login(driver)
    add_backpack(driver)
    badge = driver.find_element(By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
    assert badge.text == "1"


def test_cart_page_shows_added_item(driver):
    login(driver)
    add_backpack(driver)
    open_cart(driver)
    assert "cart.html" in driver.current_url
    assert "Sauce Labs Backpack" in cart_item_names(driver)


def test_remove_item_from_cart(driver):
    login(driver)
    add_backpack(driver)
    open_cart(driver)
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
    assert cart_item_names(driver) == []


def test_logout(driver):
    login(driver)
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    logout_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    )
    logout_link.click()
    assert driver.current_url.rstrip("/") == BASE_URL