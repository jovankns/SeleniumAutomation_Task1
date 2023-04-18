from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryItemPage:
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button[id^='add-to-cart']")
    INV_ITEM_NAME = (By.CLASS_NAME, "inventory_details_name.large_size")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def add_item_to_cart(self):
        add_to_cart_button = self.wait.until(EC.presence_of_element_located(self.ADD_TO_CART_BTN), "Add to cart button not found")
        inventory_item_name = self.driver.find_element(*self.INV_ITEM_NAME).text
        add_to_cart_button.click()
        return inventory_item_name

