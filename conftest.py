import allure
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default="chrome",
                     help="Choose browser: chrome, edge or firefox")


@pytest.fixture(scope="function")
def driver(request):
    setup_report()
    browser = request.config.getoption("browser")
    driver = None
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    driver.maximize_window()
    yield driver
    teardown_report()
    driver.quit()


@allure.step('Getting webdriver')
def setup_report():
    pass


@allure.step('Closing webdriver')
def teardown_report():
    pass