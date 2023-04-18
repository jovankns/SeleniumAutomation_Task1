import pytest
from sauce_demo.pages.login_page import LoginPage
from sauce_demo.pages.cart_page import CartPage
from sauce_demo.pages.inventory_page import InventoryPage
from sauce_demo.pages.header import Header
from sauce_demo.pages.inventory_item_page import InventoryItemPage
from sauce_demo.pages.checkout_page import CheckoutPage
from sauce_demo.pages.checkout_summary_page import CheckoutSummaryPage
from sauce_demo.pages.checkout_complete_page import CheckoutCompletePage


@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture()
def cart_page(driver):
    return CartPage(driver)


@pytest.fixture()
def inventory_page(driver):
    return InventoryPage(driver)


@pytest.fixture()
def header(driver):
    return Header(driver)


@pytest.fixture()
def inventory_item_page(driver):
    return InventoryItemPage(driver)


@pytest.fixture()
def checkout_page(driver):
    return CheckoutPage(driver)


@pytest.fixture()
def checkout_summary_page(driver):
    return CheckoutSummaryPage(driver)


@pytest.fixture()
def checkout_complete_page(driver):
    return CheckoutCompletePage(driver)
