from appium.webdriver.common.appiumby import AppiumBy
import allure
import time

class CheckInPage:
    def __init__(self, driver):
        self.driver = driver

    def perform_check_in(self):
        with allure.step("Tap Check-IN"):
            self.driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Check-IN"]').click()
            time.sleep(3)
            self.driver.save_screenshot("screenshots/checkin_step1.png")

        with allure.step("Capture photo"):
            self.driver.find_element(AppiumBy.XPATH, '//android.view.View[@resource-id="com.sec.android.app.camera:id/bottom_background"]').click()
            time.sleep(3)
            self.driver.save_screenshot("screenshots/checkin_step2.png")

        with allure.step("Confirm photo OK"):
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="OK"]').click()
            self.driver.save_screenshot("screenshots/checkin_step3.png")

        with allure.step("Tap Check-OUT to confirm"):
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Check-IN"]').click()
            time.sleep(2)
            self.driver.save_screenshot("screenshots/checkin_step4.png")
