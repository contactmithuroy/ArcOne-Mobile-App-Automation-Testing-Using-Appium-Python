# 📱 Appium Test Automation (Android) — POM + Allure + Python
This repository contains an automated test suite for an Android HR application using **Appium**, **Python**, **Pytest**, and **Allure** reporting, structured with the 
**Page Object Model (POM)** design pattern. Each test includes **step-wise screenshots** for better traceability and debugging.
---
## Test Cases Included

| Test File                     | Description                                             |
|------------------------------|---------------------------------------------------------|
| `test_login.py`              | Automates login functionality using valid credentials   |
| `test_attendance_report.py`  | Searches attendance records by date and status          |
| `test_check_in.py`           | Simulates employee check-in with camera integration     |
| `test_leave_application.py`  | Automates the leave application submission process      |

---
## Prerequisites 
Before running the tests, ensure the following:
- Python 3.8 or above installed
- Java JDK installed and added to PATH
- Appium server installed and running (GUI or CLI)
- Android SDK and ADB configured correctly
- A physical Android device connected with USB debugging enabled
-  Node version is 18.17.1
- Path Environment:
  - NodeJS: C:\Program Files\nodejs\node.EXE
  - ANDROID_HOME: C:\Users\MITHU\AppData\Local\Android\Sdk
  - %ANDROID_HOME%\platform-tools
  - %ANDROID_HOME%\build-tools
  - %ANDROID_HOME%\tools
  - JAVA_HOME: C:\Program Files\Java\jdk-23
  
## Dependencies
requirements.txt
  - Appium-Python-Client==3.1.1
  - pytest==7.4.0
  - pytest-order==1.2.0
  - allure-pytest==2.13.2
---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/contactmithuroy/ArcOne-Mobile-App-Automation-Testing-Using-Appium-Python.git)

2. Install dependencies:
3. ```bash
   pip install -r requirements.txt

- Install Allure (if not already installed):

3. How to Run the Tests
  - Start Appium Server (ensure it's listening at http://localhost:4723/wd/hub)
  - Connect your Android device ( Enable USB Debugging with revoke authorisation in Developer mode on Device) 

### Run the tests in the project:
1. ```bash
   pytest --alluredir=allure-results
### Generate and view Allure report:
1. ```bash
   allure generate reports/ -o allure-report/ --clean
   allure serve allure-results

###Additional Info
  - Execution order of tests is maintained using pytest-order.
  - Screenshots for each step are saved automatically in the screenshots/ folder.
  - Login is performed first as a precondition for other tests.

# Output of Allure Report:

<img width="1043" height="293" alt="ss5" src="https://github.com/user-attachments/assets/a4de9d01-25d7-496e-abbe-0d1b62e0ad14" />
<img width="751" height="376" alt="ss4" src="https://github.com/user-attachments/assets/183bb16e-94a9-4b4e-9094-0d76e6856509" />

📁 Project Structure
```bash
project-root/
├── pages/                     
│   ├── login_page.py
│   ├── attendance_page.py
│   └── checkin_page.py
│   └── leave_page.py
├── tests/                     
│   ├── test_login.py
│   ├── test_attendance_report.py
│   ├── test_check_in.py
│   └── test_leave_application.py
├── utils/
│   └── capabilities.py        
├── screenshots/               
├── conftest.py                
├── requirements.txt           
└── README.md                 
   
