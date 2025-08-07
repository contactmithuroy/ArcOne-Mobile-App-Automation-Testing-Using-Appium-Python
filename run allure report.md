
#Run the test case:
pytest --alluredir=allure-results

#Run test cases with allure report:
allure generate reports/ -o allure-report/ --clean

#Open the allure Result:
allure open allure-report/

