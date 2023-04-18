from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    ZIP_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def enter_first_name(self, first):
        first_name = self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_INPUT), "First name input field not found")
        first_name.send_keys(first)

    def enter_last_name(self, last):
        last_name = self.wait.until(EC.visibility_of_element_located(self.LAST_NAME_INPUT), "Last name input field not found")
        last_name.send_keys(last)

    def enter_zip(self, postal_code):
        zip_code = self.wait.until(EC.visibility_of_element_located(self.ZIP_CODE_INPUT), "Zip/Postal Code input field not found")
        zip_code.send_keys(postal_code)

    def click_continue_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON), "Continue button not found").click()
