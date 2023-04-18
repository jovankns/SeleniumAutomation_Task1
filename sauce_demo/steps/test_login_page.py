import logging
from pytest_bdd import scenarios, given, when, then, parsers

# Initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the scenarios from the feature files
scenarios('../features/login.feature')


# Define given steps
@given(parsers.parse('Go to "{url}"'))
def go_to_url(url, login_page):
    login_page.navigate_to_page(url)
    logger.info(f"Navigating to {url}")


# Define when steps
@when('the user not enter an email address')
def user_not_enter_email(login_page):
    login_page.enter_email("")
    logger.info("User does not enter an email address")


@when('the user not enter a password')
def user_not_enter_password(login_page):
    login_page.enter_password("")
    logger.info("User does not enter a password")


@when("the user enter an email address")
def user_enter_an_email_address(login_page, stand_user):
    logger.info(f"User enters email address: {stand_user}")
    login_page.enter_email(stand_user)


@when('the user enter a password')
def user_enter_a_password(login_page, password):
    login_page.enter_password(password)
    logger.info(f"User enters password: {password}")


@when('the user click the Login button')
def user_click_login_button(login_page):
    login_page.click_login_button()
    logger.info("User clicks Login button")


@when('the user enter a valid email address')
def enter_valid_email(login_page, stand_user):
    login_page.enter_email(stand_user)
    logger.info(f"User enters valid email address: {stand_user}")


@when(parsers.parse('the user enter the email address, "{email_address}"'))
def user_enter_email(login_page, email_address):
    login_page.enter_email(email_address)
    logger.info(f"User enters email address: {email_address}")


@when('the user enter a valid password')
def user_enter_valid_password(login_page, password):
    login_page.enter_password(password)
    logger.info(f"User enters valid password: {password}")


@when('the user enter the wrong password')
def user_enter_wrong_password(login_page):
    login_page.enter_password("WrongPassword")
    logger.info("User enters wrong password")


@when('the user clicks the Login button')
def user_clicks_login_button(login_page):
    login_page.click_login_button()
    logger.info("User clicks Login button")


# Define then steps
@then(parsers.parse('the error says, "{expected_error}"'))
def error_displays(login_page, expected_error):
    assert expected_error == login_page.get_login_error_text()
    logger.info(f"Verifying error message: {expected_error}")


@then(parsers.parse('the error says, "{expected_error}"'))
def error_says(login_page, expected_error):
    assert expected_error == login_page.get_login_error_text()
    logger.info(f"Verifying error message: {expected_error}")


@then('the Inventory Page displays')
def inventory_page_displays(inventory_page):
    inventory_page.verify_inventory_page_is_displayed()
    logger.info("Verifying that the Inventory Page is displayed")
