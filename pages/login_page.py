from appium.webdriver.common.appiumby import AppiumBy
import allure
import time
import os

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        with allure.step("Enter email"):
            email_field = self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Enter Email"]')
            if not email_field:
                self.driver.save_screenshot("screenshots/error_email_field_not_found.png")
                raise AssertionError("Email input field not found")
            email_field.send_keys(email)

        with allure.step("Enter password"):
            password_field = self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Enter Password"]')
            if not password_field:
                self.driver.save_screenshot("screenshots/error_password_field_not_found.png")
                raise AssertionError("Password input field not found")
            password_field.send_keys(password)

        with allure.step("Tap login button"):
            login_btn = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Login"]')
            if not login_btn:
                self.driver.save_screenshot("screenshots/error_login_button_not_found.png")
                raise AssertionError("Login button not found")
            login_btn.click()

        self.driver.save_screenshot("screenshots/Successfully_login.png")

        time.sleep(10)
