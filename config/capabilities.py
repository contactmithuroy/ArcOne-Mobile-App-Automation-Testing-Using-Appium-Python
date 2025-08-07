from appium import webdriver
from appium.options.android import UiAutomator2Options

def get_driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.platform_version = "14"  # Replace with  device version
    options.device_name = "RZCW20XTW5M"  # Replace with actual device ID
    options.automation_name = "UiAutomator2"
    options.app_package = "com.arcone.arcone" # App package Name
    options.app_activity = "com.arcone.arcone.MainActivity" # App acivity name
    options.no_reset = True

    return webdriver.Remote("http://localhost:4723/wd/hub", options=options)
