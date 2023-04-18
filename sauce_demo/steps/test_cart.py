import logging
import pytest
from pytest_bdd import scenarios, given, when, then, parsers

# Initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the scenarios from the feature files
scenarios('../features/cart.feature')


# Create an empty list for storing the names of the items added to the cart
@pytest.fixture
def items_list():
    return []


@given(parsers.parse('Go to "{url}"'))
def go_to_url(url, login_page):
    login_page.navigate_to_page(url)
    logger.info(f"Navigated to {url}")


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


@then("the cart badge is updated correctly")
def verify_cart_badge(header, items_list):
    header.verify_cart_badge_count_is_displayed()
    cart_count = int(header.get_cart_badge_count())
    items_count = len(items_list)
    assert cart_count == items_count
    logger.info(f"Verified that cart badge count '{cart_count}' is updated correctly for '{items_count}' items in cart")


@then("the correct items are present")
def verify_cart_items(cart_page, items_list):
    cart_page.verify_cart_items(items_list)
    logger.info("Verified that the correct items are present in the cart")
