import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver


# to take screenshot
# get_screenshot_as_png()

@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if "rep_call" in item.__dict__ and item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot_on_failure", attachment_type=AttachmentType.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(params=["chrome"], scope="function")
def init_driver(request):
    global driver
    driver = None
    try:
        if request.param == "chrome":
            driver = webdriver.Chrome()
    except Exception as e:
        print(f'Error occurred while creating the driver: {e}')
    if driver:
        request.cls.driver = driver
        yield
        driver.close()
    else:
        raise RuntimeError("Driver not initialized")
