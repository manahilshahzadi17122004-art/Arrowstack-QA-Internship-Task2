# # Arrowstack QA Internship - Task 2

Automated End-to-End Test Suite for the SauceDemo web portal
(https://www.saucedemo.com) using Selenium WebDriver and pytest,
completed as part of the Arrowstack Software Testing & QA virtual internship.

## What is tested
- Login: valid login, wrong password, empty username, empty password, locked-out user
- Shopping flow: add item (cart badge), cart page shows item, remove item, logout

Total: 9 automated tests. These automate selected cases from the manual
test suite in Task 1.

## Files
- conftest.py - Chrome browser setup (pytest fixture)
- test_login.py - 5 login tests
- test_shopping_flow.py - 4 end-to-end cart and logout tests
- report.html - pytest HTML test report
- report_screenshot.png - screenshot of the HTML test report

## Result
9 passed (see report.html).

## How to run
1. Install Python 3.11 and Google Chrome.
2. pip install selenium pytest pytest-html
3. pytest -v --html=report.html --self-contained-html

Selenium 4 downloads the Chrome driver automatically, so an internet
connection is needed on the first run.

## Tools
Python 3.11, Selenium 4.51.0, pytest 9.1.1, pytest-html 4.2.0, Google Chrome

## Limitations
Only Chrome was used. Only 9 of the 43 manual test cases are automated.
Tests depend on the live SauceDemo site, so a site change can break them.
