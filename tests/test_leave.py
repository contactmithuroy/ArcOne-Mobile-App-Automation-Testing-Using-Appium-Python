import pytest
from pages.leave_page import LeavePage

@pytest.mark.order(4)
def test_leave_application(setup):
    LeavePage(setup).apply_leave()
