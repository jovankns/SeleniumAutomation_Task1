from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutSummaryPage:
    FINISH_BUTTON = (By.ID, "finish")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def click_finish_button(self):
        self.wait.until(EC.element_to_be_clickable(self.FINISH_BUTTON), "Continue button not found").click()
