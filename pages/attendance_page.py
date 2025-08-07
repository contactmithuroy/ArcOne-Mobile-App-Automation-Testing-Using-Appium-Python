from appium.webdriver.common.appiumby import AppiumBy
import allure
import time
import os

class AttendancePage:
    def __init__(self, driver):
        self.driver = driver

    def search_attendance(self):
        with allure.step("Tap 'My Attendance' from dashboard"):
            attendance_button = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="My Attendance"]')
            assert attendance_button is not None, "'My Attendance' button not found"
            attendance_button.click()
            time.sleep(1)

        with allure.step("Select From Date: 01 August 2025"):
            from_date = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="From"]')
            assert from_date is not None, "'From Date' field not found"
            from_date.click()
            self.driver.find_element(AppiumBy.XPATH, '//android.view.View[@content-desc="01 August 2025"]').click()
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="OK"]').click()

        with allure.step("Select To Date: 15 August 2025"):
            to_date = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="To"]')
            assert to_date is not None, "'To Date' field not found"
            to_date.click()
            self.driver.find_element(AppiumBy.XPATH, '//android.view.View[@content-desc="15 August 2025"]').click()
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="OK"]').click()

        with allure.step("Filter attendance by 'Present' status"):
            status_dropdown = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="All"]')
            assert status_dropdown is not None, "'Status' filter not found"
            status_dropdown.click()
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Present"]').click()
            time.sleep(2)

        with allure.step("Validate attendance results contain 'Present'"):
            results = self.driver.find_elements(AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "Present")]')
            assert results, "No attendance results found for 'Present'"
            self.driver.save_screenshot("screenshots/Attendance_report_results.png")
