import json
import os
import logging
import pytest
import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Add custom command line options for pytest
def pytest_addoption(parser):
    parser.addoption("--runner", action="store", default="local", help="set the test suite to run on Selenium Grid")
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name (chrome, firefox, edge)")


# Fixture for getting the test runner type (local or remote)
@pytest.fixture
def runner(request):
    return request.config.getoption("--runner")


# Fixture for getting the browser type to use for the test
@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


# Fixture for creating the webdriver instance
@pytest.fixture
def driver(runner, browser):
    # Check the test runner type and create the appropriate webdriver instance
    if runner == "local":
        # Set up webdriver options for the local machine
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--window-size=1360,768")
        options.headless = os.environ.get("HEADLESS_FLAG", "False") == "True"
        if browser == 'chrome':
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        elif browser == 'firefox':
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif browser == 'edge':
            driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
        else:
            raise Exception(f"{browser} is not supported")
    elif runner == "remote":
        # Set up webdriver options for a remote Selenium Grid instance
        capabilities = webdriver.DesiredCapabilities.CHROME.copy()
        capabilities['platform'] = 'WINDOWS'
        capabilities['version'] = '10'

        remote_url = 'http://localhost:4444/wd/hub'
        driver = webdriver.Remote(
            command_executor=remote_url,
            desired_capabilities=capabilities
        )

    # Log the initialized driver instance
    logging.info(f"Initialized {browser} driver")
    # Return the webdriver instance to the test
    yield driver
    # Close the webdriver instance and log the test completion
    driver.close()
    driver.quit()
    logging.info("Test completed")


# Hook for taking a screenshot when a test fails
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        try:
            feature_request = item.funcargs["request"]
            driver = feature_request.getfixturevalue("driver")
        except KeyError:
            return
        screenshot_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "screenshots")
        os.makedirs(screenshot_dir, exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = os.path.join(screenshot_dir, f"screenshot-{timestamp}.png")
        driver.save_screenshot(screenshot_path)


# Fixture for loading configuration data from a JSON file
@pytest.fixture
def config():
    config_path = os.path.dirname(os.path.realpath(__file__)) + "/config.json"
    with open(config_path) as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture
def base_url(config):
    return config["base_url"]


@pytest.fixture
def stand_user(config):
    return config["stand_user"]


@pytest.fixture
def lock_user(config):
    return config["lock_user"]


@pytest.fixture
def password(config):
    return config["password"]
