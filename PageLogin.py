from selenium.webdriver.common.by import By
import time

class Page_Login:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = "//input[@placeholder='Enter email']"
        self.password_locator = "//input[@placeholder='Enter Password']"
        self.login_button_locator = "//button[normalize-space()='LOGIN']"

    def enter_username(self, username):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.username_locator).click()
        self.driver.find_element(By.XPATH, self.username_locator).send_keys(username)

    def enter_password(self, password):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.password_locator).click()
        self.driver.find_element(By.XPATH, self.password_locator).send_keys(password)

    def click_login(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.login_button_locator).click()
        time.sleep(5)



