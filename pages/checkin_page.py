from appium.webdriver.common.appiumby import AppiumBy
import allure
import time
import os

class CheckInPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def perform_check_in(self):
        with allure.step("Tap Check-IN"):
            check_in_button = self.driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Check-IN"]')
            assert check_in_button is not None, "Check-IN button not found"
            check_in_button.click()
            time.sleep(3)

        with allure.step("Capture photo"):
            camera_btn = self.driver.find_element(AppiumBy.XPATH, '//android.view.View[@resource-id="com.sec.android.app.camera:id/bottom_background"]')
            assert camera_btn is not None, "Camera button not found"
            camera_btn.click()
            time.sleep(3)

        with allure.step("Confirm photo OK"):
            ok_btn = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="OK"]')
            assert ok_btn is not None, "OK button after photo not found"
            ok_btn.click()
        
        with allure.step("Enter Log Type"):
            #//android.view.ViewGroup[@content-desc="IN, Log Type"]/android.view.ViewGroup[1]
            log_type = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="IN"]')
            assert log_type is not None, "Log type 'IN' not found"
            log_type.click()

            log_type_name = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="IN"]')
            log_type_name.click()
            time.sleep(2)

        with allure.step("Tap Check-IN to confirm"):
            confirm_checkin = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Check-IN"]')
            assert confirm_checkin is not None, "Final Check-IN confirmation button not found"
            confirm_checkin.click()
            time.sleep(3)
            
            self.driver.save_screenshot("screenshots/Successfully Check In.png")

        with allure.step("Handle confirmation popup"):
            success_msg = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Checked IN Successful"]')
            assert success_msg is not None, "'Checked IN Successful' message not found"

            ok_popup_btn = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="OK"]')
            assert ok_popup_btn is not None, "Popup OK button not found"
            ok_popup_btn.click()

        