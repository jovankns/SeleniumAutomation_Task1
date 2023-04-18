import random

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    TITLE = (By.CLASS_NAME, "title")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button[id^='add-to-cart']")
    INV_ITEM_NAME_FROM_BTN = (By.XPATH, "./ancestor::div[@class='inventory_item']//div[@class='inventory_item_name']")
    PRODUCT_LIST = (By.CSS_SELECTOR, "div.inventory_item")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def verify_inventory_page_is_displayed(self):
        title = self.wait.until(EC.element_to_be_clickable(self.TITLE))
        return title.is_displayed()

    def add_random_item_to_cart(self):
        try:
            add_to_cart_buttons = self.wait.until(EC.presence_of_all_elements_located(self.ADD_TO_CART_BTN))
        except NoSuchElementException:
            raise NoSuchElementException("Any add to cart buttons not found")
        add_to_cart_button = random.choice(add_to_cart_buttons)
        inventory_item_name = add_to_cart_button.find_element(*self.INV_ITEM_NAME_FROM_BTN).text
        add_to_cart_button.click()
        return inventory_item_name

    def open_item_details_page(self):
        try:
            add_to_cart_buttons = self.wait.until(EC.presence_of_all_elements_located(self.ADD_TO_CART_BTN))
        except NoSuchElementException:
            raise NoSuchElementException("Any add to cart buttons not found")
        add_to_cart_button = random.choice(add_to_cart_buttons)
        inventory_item_name = add_to_cart_button.find_element(*self.INV_ITEM_NAME_FROM_BTN)
        inventory_item_name.click()
