import pytest
from pages.checkin_page import CheckInPage

@pytest.mark.order(3)
def test_checkin(setup):
    CheckInPage(setup).perform_check_in()
