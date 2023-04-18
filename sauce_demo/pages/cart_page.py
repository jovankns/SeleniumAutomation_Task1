from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def remove_item_from_cart(self, item_name):
        self.wait.until(EC.presence_of_element_located((By.XPATH, f"//div[text()='{item_name}']")),
                        f"Can't find first item with name {item_name}")
        button_id = 'remove-' + item_name.lower().replace(' ', '-')
        try:
            remove_button = self.driver.find_element(By.ID, button_id)
            remove_button.click()
        except NoSuchElementException:
            raise NoSuchElementException(f"Can't find remove button with ID '{button_id}'")

    def get_cart_item_names(self):
        item_name_elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.CART_ITEM_NAME))
        if not item_name_elements:
            print("No item found in cart")
            return []
        item_names = [item_name.text for item_name in item_name_elements]
        return item_names

    def verify_cart_items(self, expected_item_names):
        actual_item_names = self.get_cart_item_names()
        assert actual_item_names == expected_item_names, f"Expected items: {expected_item_names}, but got: {actual_item_names}"

    def click_checkout_button(self):
        checkout_button = self.wait.until(EC.visibility_of_element_located(self.CHECKOUT_BUTTON), "Checkout button not found")
        checkout_button.click()
