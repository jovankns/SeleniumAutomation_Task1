from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    SWAG_LABS_LOGO = (By.CLASS_NAME, 'login_logo')
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, 'login-button')
    ERROR = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def navigate_to_page(self, url):
        self.driver.get(url)

    def enter_email(self, email):
        email_input = self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT),
                                      "Username input field not found")
        email_input.send_keys(email)

    def enter_password(self, password):
        password_input = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT),
                                         "Password input field not found")
        password_input.send_keys(password)

    def click_login_button(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON), "Login button not found").click()

    def get_login_error_text(self):
        login_error_alert = self.wait.until(EC.visibility_of_element_located(self.ERROR), "Login error alert not found")
        return login_error_alert.text
