from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Header:
    CART_LINK = (By.ID, "shopping_cart_container")
    CART_COUNT = (By.CLASS_NAME, "shopping_cart_badge")
    REMOVE_BUTTONS = (By.CSS_SELECTOR, ".cart_item .cart_button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def verify_cart_badge_count_is_displayed(self):
        cart_count = self.wait.until(EC.visibility_of_element_located(self.CART_COUNT), "Cart badge count not found")
        return cart_count.is_displayed()

    def get_cart_badge_count(self):
        return self.driver.find_element(*self.CART_COUNT).text

    def click_on_cart(self):
        cart_link = self.wait.until(EC.visibility_of_element_located(self.CART_LINK), "Cart not found")
        return cart_link.click()
