import pytest
from pages.attendance_page import AttendancePage

@pytest.mark.order(2)
def test_attendance_search(setup):
    AttendancePage(setup).search_attendance()
