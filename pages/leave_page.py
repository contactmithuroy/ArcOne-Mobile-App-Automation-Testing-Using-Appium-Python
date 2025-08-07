from appium.webdriver.common.appiumby import AppiumBy
import allure
import time
import os

class LeavePage:
    def __init__(self, driver):
        self.driver = driver

    def apply_leave(self):
        with allure.step("Tap Leave Application"):
            leave_app_btn = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Leave Application"]')
            assert leave_app_btn is not None, "Leave Application button not found"
            leave_app_btn.click()

        with allure.step("Tap New Application"):
            new_app_btn = self.driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc=""]')
            assert new_app_btn is not None, "New Application button not found"
            new_app_btn.click()

        try:
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Application"]').click()
        except:
            pass

        with allure.step("Select Leave Type"):
            leave_type_field = self.driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc=", Leave Type*"]/android.view.ViewGroup')
            assert leave_type_field is not None, "Leave Type field not found"
            leave_type_field.click()
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Annual Leave"]').click()

        with allure.step("Select From Date"):
            self.driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc=", From Date*"]').click()
            self.driver.find_element(AppiumBy.XPATH, '//android.view.View[@content-desc="06 August 2025"]').click()
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="OK"]').click()

        with allure.step("Select To Date"):
            self.driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc=", To Date*"]').click()
            self.driver.find_element(AppiumBy.XPATH, '//android.view.View[@content-desc="08 August 2025"]').click()
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="OK"]').click()

        with allure.step("Enter Reason"):
            reason_field = self.driver.find_element(AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[3]')
            assert reason_field is not None, "Reason input field not found"
            reason_field.send_keys("Family emergency")

        with allure.step("Tap Apply"):
            apply_btn = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Apply"]')
            assert apply_btn is not None, "Apply button not found"
            apply_btn.click()
            time.sleep(3)
            self.driver.save_screenshot("screenshots/leave_application_confirm.png")
