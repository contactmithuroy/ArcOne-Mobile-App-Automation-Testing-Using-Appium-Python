from appium.webdriver.common.appiumby import AppiumBy
import allure
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        with allure.step("Enter email"):
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Enter Email"]').send_keys(email)
            self.driver.save_screenshot("screenshots/step1_email.png")

        with allure.step("Enter password"):
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Enter Password"]').send_keys(password)
            self.driver.save_screenshot("screenshots/step2_password.png")

        with allure.step("Tap login button"):
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Login"]').click()
            self.driver.save_screenshot("screenshots/step3_login.png")
            time.sleep(15)
