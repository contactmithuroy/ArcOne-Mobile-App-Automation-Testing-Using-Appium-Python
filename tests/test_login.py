import pytest
from pages.login_page import LoginPage

@pytest.mark.order(1)
def test_login(setup):
    login = LoginPage(setup)
    login.login("azmin@excelbd.com", "D!m77(2SJ,5j")
