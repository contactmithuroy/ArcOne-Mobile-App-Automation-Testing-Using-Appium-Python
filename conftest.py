import pytest
from config.capabilities import get_driver

@pytest.fixture(scope="function")
def setup(request):
    driver = get_driver()
    driver.implicitly_wait(10)

    # Attach driver to the test class if using class-based Page Objects
    if request.cls is not None:
        request.cls.driver = driver

    yield driver

    driver.quit()
