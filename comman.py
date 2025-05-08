import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Commons:
    search_field = "//input[@placeholder='Search']"
    date_filter_btn = "cursor-pointer"
    tm_filter_btn = "ng-select-container"
    sort_filter_btn = "//ng-select[@role='listbox' and @bindLabel='name']"

    def __init__(self, driver):
        self.driver = driver

    def search_web(self,text):
        ele = self.driver.find_element(By.XPATH, self.search_field)
        ele.clear()
        ele.send_keys(text)

    def date_filter(self):
        self.driver.find_element(By.CLASS_NAME, self.date_filter_btn).click()
        time.sleep(2)
        #self.driver.find_element(By.XPATH, "//button[text()=' Apply ']").click()

    def tm_filter(self,tm):
        self.driver.find_element(By.CLASS_NAME, self.tm_filter_btn).click()
        self.driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys(tm)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//div[@role ='option']").click()
        time.sleep(3)
        '''
        or
        self.driver.find_element(By.CLASS_NAME, self.tm_filter_btn).click()
        tms = self.driver.find_elements(By.XPATH,"//div[@class='ng-option' and @role ='option']")
        for i in tms:
            if i.text == tm:
                i.click()
                break
        '''

    def sort_filter(self):
        self.driver.find_element(By.XPATH, self.sort_filter_btn).click()
        time.sleep(2)
        li = self.driver.find_elements(By.XPATH,"//div[@role='option' and @aria-selected='false']")
        ele = random.choice(li)
        print(ele.text + " is clicked")      
        ele.click()