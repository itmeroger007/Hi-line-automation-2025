from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from PageLogin import Page_Login
from PageProspect import Page_Prospect
from PageProspect import add_pros
import time

CHROMEDRIVER_PATH = "C:/Users/Bhuvnesh/Desktop/Hiline P21 Automtion/PageObject/chromedriver.exe"

class AutomationTest:
    def __init__(self, driver_path):
        service = Service(driver_path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def run_test(self, url, username, password):
            self.driver.get(url)
            time.sleep(4)
            
            login_page = Page_Login(self.driver)
            login_page.enter_username(username)
            login_page.enter_password(password)
            login_page.click_login()
            

            prospect_module = Page_Prospect(self.driver)
            prospect_module.open_prospect_module()


            prospect_module = add_pros(self.driver)
            prospect_module.add_new_Prospect()

            # prospects_page.click_first_entry()
        
        # except Exception as e:
        #     print("An error occurred:", e)
        # finally:
        #     self.driver.quit()

if __name__ == "__main__":
    automation = AutomationTest(driver_path=CHROMEDRIVER_PATH)
    automation.run_test(
        url="https://p21core.hi-line.com/uat/console/",
        username="anil.p@copperdigital.com",
        password="Anil@123"
    )