from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutCompletePage:
    THANK_TEXT = (By.CLASS_NAME, "complete-header")
    COMPLETE_TEXT = (By.CLASS_NAME, "complete-text")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def is_checkout_complete_page_displayed(self):
        thank_text = self.wait.until(EC.visibility_of_element_located(self.THANK_TEXT), "Thank text not found")
        complete_text = self.wait.until(EC.visibility_of_element_located(self.COMPLETE_TEXT), "Complete text not found")
        return thank_text.is_displayed() and complete_text.is_displayed()
