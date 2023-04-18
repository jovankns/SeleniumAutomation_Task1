import logging
import pytest
from pytest_bdd import given, when, then, scenarios, parsers

# Initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the scenarios from the feature files
scenarios("../features/complete_order.feature")


# Create an empty list for storing the names of the items added to the cart
@pytest.fixture
def items_list():
    return []


# Define given steps
@given(parsers.parse('Go to "{url}"'))
def go_to_url(url, login_page):
    login_page.navigate_to_page(url)
    logger.info(f"Navigated to {url}")


# Define when steps
@when("I log in to the site")
def login_to_site(login_page, stand_user, password, inventory_page, items_list):
    login_page.enter_email(stand_user)
    login_page.enter_password(password)
    login_page.click_login_button()
    inventory_page.verify_inventory_page_is_displayed()
    items_list.clear()
    logger.info(f"Logged in to the site with username '{stand_user}' and password '{password}'")


@when("I add random item from the list to the cart")
def add_random_item_to_cart(inventory_page, items_list):
    item = inventory_page.add_random_item_to_cart()
    items_list.append(item)
    logger.info(f"Added item '{item}' to the cart")


@when("I open item's details page")
def open_item_details_page(inventory_page):
    inventory_page.open_item_details_page()
    logger.info("Opened item's details page")


@when("I add the item to the cart")
def add_item_to_cart(inventory_item_page, items_list):
    item = inventory_item_page.add_item_to_cart()
    items_list.append(item)
    logger.info(f"Added item '{item}' to the cart")


@when("I open the cart")
def open_cart(header):
    header.click_on_cart()
    logger.info("Opened the cart")


@when("I remove the first item from the cart")
def remove_first_item_from_cart(cart_page, items_list):
    item = items_list.pop(0)
    cart_page.remove_item_from_cart(item)
    logger.info(f"Removed item '{item}' from the cart")


@when("I continue to the Checkout page")
def continue_to_checkout(cart_page):
    cart_page.click_checkout_button()
    logger.info("Clicked on Checkout button")


@when("I complete the checkout form")
def complete_checkout_form(checkout_page):
    checkout_page.enter_first_name("first")
    checkout_page.enter_last_name("last")
    checkout_page.enter_zip("zip")
    checkout_page.click_continue_button()
    logger.info("Filled out the checkout form")


@when("I complete the order")
def complete_order(checkout_summary_page):
    checkout_summary_page.click_finish_button()
    logger.info("Clicked on Finish button")


# Define then steps
@then("the order is completed successfully with the displayed message")
def verify_order_completed(checkout_complete_page):
    assert checkout_complete_page.is_checkout_complete_page_displayed()
    logger.info("Order completed successfully")
