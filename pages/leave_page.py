from appium.webdriver.common.appiumby import AppiumBy
import allure
import time

class LeavePage:
    def __init__(self, driver):
        self.driver = driver

    def apply_leave(self):
        with allure.step("Tap Leave Application"):
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Leave Application"]').click()
            self.driver.save_screenshot("screenshots/leave_step1.png")

        with allure.step("Tap New Application"):
            self.driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc=""]').click()
            self.driver.save_screenshot("screenshots/leave_step2.png")

        try:
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Application"]').click()
        except:
            pass

        with allure.step("Select Leave Type"):
            self.driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc=", Leave Type*"]/android.view.ViewGroup').click()
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Annual Leave"]').click()
            self.driver.save_screenshot("screenshots/leave_step3.png")

        with allure.step("Select From Date"):
            self.driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc=", From Date*"]').click()
            self.driver.find_element(AppiumBy.XPATH, '//android.view.View[@content-desc="06 August 2025"]').click()
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="OK"]').click()
            self.driver.save_screenshot("screenshots/leave_step4.png")

        with allure.step("Select To Date"):
            self.driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc=", To Date*"]').click()
            self.driver.find_element(AppiumBy.XPATH, '//android.view.View[@content-desc="08 August 2025"]').click()
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="OK"]').click()
            self.driver.save_screenshot("screenshots/leave_step5.png")

        with allure.step("Enter Reason"):
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[3]').send_keys("Family emergency")
            self.driver.save_screenshot("screenshots/leave_step6.png")

        with allure.step("Tap Apply"):
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Apply"]').click()
            time.sleep(3)
            self.driver.save_screenshot("screenshots/leave_step7.png")
