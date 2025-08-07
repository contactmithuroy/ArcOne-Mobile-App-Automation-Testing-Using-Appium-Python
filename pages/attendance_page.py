from appium.webdriver.common.appiumby import AppiumBy
import allure
import time
import os

class AttendancePage:
    def __init__(self, driver):
        self.driver = driver

    def search_attendance(self):
        with allure.step("Tap My Attendance"):
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="My Attendance"]').click()
            self.driver.save_screenshot("screenshots/att_step1.png")

        with allure.step("Select From Date"):
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="From"]').click()
            self.driver.find_element(AppiumBy.XPATH, '//android.view.View[@content-desc="01 August 2025"]').click()
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="OK"]').click()
            self.driver.save_screenshot("screenshots/att_step2.png")

        with allure.step("Select To Date"):
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="From"]').click()
            self.driver.find_element(AppiumBy.XPATH, '//android.view.View[@content-desc="15 August 2025"]').click()
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="OK"]').click()
            self.driver.save_screenshot("screenshots/att_step3.png")

        with allure.step("Filter by status"):
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="All"]').click()
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Present"]').click()
            self.driver.save_screenshot("screenshots/att_step4.png")

        with allure.step("Validate attendance result"):
            results = self.driver.find_elements(AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "Present")]')
            assert len(results) > 0, "No attendance found"
            self.driver.save_screenshot("screenshots/att_step5_results.png")
