from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
import time
# import select

class Page_Prospect:
    def __init__(self, driver):
        self.driver = driver
        self.prospect_module_locator = "//span[normalize-space()='Prospects Inquiry']"
        # self.first_entry_css = "//h6[contains(text(), 'krishna')]"  # CSS Selector for first entry

    def open_prospect_module(self):
        prospect_module = self.driver.find_element(By.XPATH, self.prospect_module_locator)
        prospect_module.click()
        time.sleep(5)
        print("Clicked on the Prospects Inquiry module successfully.")

class add_pros:
    def __init__(self, driver):
            self.driver = driver
            self.add_locator = "//button[normalize-space()='Add Prospect']"


    def add_new_Prospect(self):
            new_pros = self.driver.find_element(By.XPATH, self.add_locator)
            new_pros.click()
            time.sleep(5)
    def add_prosp(self,tm,prosp_name,prosp_mno,prosp_add,prosp_city,prosp_zip,prosp_state,prosp_f_name,prosp_l_name):
        # self.driver.find_element(By.XPATH, self.add_prosp_btn).click()
        # time.sleep(2)
        self.tm_filter(tm)
        self.driver.find_element(By.XPATH,"//input[@placeholder='Enter Name']").send_keys(prosp_name)
        self.driver.find_element(By.XPATH,"//input[@placeholder='Enter Phone']").send_keys(prosp_mno)
        self.driver.find_element(By.XPATH,"//input[@placeholder='Enter address']").send_keys(prosp_add)
        self.driver.find_element(By.XPATH,"//input[@placeholder='Enter city']").send_keys(prosp_city)
        self.driver.find_element(By.XPATH,"//input[@placeholder='Enter zipcode']").send_keys(prosp_zip)
        self.driver.find_element(By.XPATH,"//*[@bindlabel='state']").click()
        self.driver.find_element(By.XPATH,f"//*[text()='{prosp_state}']").click()
        self.driver.find_element(By.XPATH,"(//*[@bindlabel='description'])[1]").click()
        self.driver.find_element(By.XPATH,"//*[contains(text(),'Gas')]").click()
        self.driver.find_element(By.XPATH,"(//*[@bindlabel='description'])[2]").click()
        self.driver.find_element(By.XPATH,"//*[contains(text(),'RATTLEBOX')]").click()
        ele = self.driver.find_element(By.XPATH,"//h4[text()='Prospect Info']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);",ele)
        ele = self.driver.find_element(By.XPATH,"(//label[@class='item'])[3]")
        ele.click()
        self.driver.execute_script("arguments[0].scrollIntoView(true);",ele)
        self.driver.find_element(By.XPATH,"//input[@placeholder='Enter first name']").send_keys(prosp_f_name)
        self.driver.find_element(By.XPATH,"//input[@placeholder='Enter last name']").send_keys(prosp_l_name)
        self.driver.find_element(By.XPATH,"(//*[@bindlabel='description'])[3]").click()
        self.driver.find_element(By.XPATH,"//*[contains(text(),'OWNER')]").click()
        ele = self.driver.find_element(By.XPATH,"(//*[@bindlabel='description'])[4]")
        self.driver.execute_script("arguments[0].scrollIntoView(true);",ele)
        ele.click()
        self.driver.find_element(By.XPATH,"//*[contains(text(),'TXMAS')]").click()
        self.driver.find_element(By.XPATH,"(//*[@bindlabel='description'])[5]").click()
        self.driver.find_element(By.XPATH,"(//*[contains(text(),'TXMAS')])[2]").click()
        self.driver.find_element(By.XPATH,"//button[text()='Save']").click()

    def open_prosp_detail(self):
        self.driver.find_element(By.XPATH, self.prosp_detail).click()
    
    # def owl_date_picker(self,i):
    #     if i == 0:
    #         self.driver.find_element(By.XPATH,"(//span[@class='ctTimeBox'])[1]").click()
    #         date_obj = datetime.date.today() 
    #     elif i == 1:
    #         self.driver.find_element(By.XPATH,"(//span[@class='ctTimeBox'])[2]").click()
    #         date_obj = datetime.date.today() + datetime.timedelta(days=1) 
    #     else:
    #         self.driver.find_element(By.XPATH,"(//span[@class='ctTimeBox'])[3]").click()
    #         date_obj = datetime.date.today() + datetime.timedelta(days=2) 
    #     tmp_month = date_obj.strftime("%B")
    #     tmp_no = date_obj.strftime("%d")
    #     tmp_yr = date_obj.strftime("%Y")
    #     tmp_date = f"//td[contains(@aria-label,'{tmp_month} {tmp_no}, {tmp_yr}')]"
    #     time.sleep(1)
    #     self.driver.find_element(By.XPATH,tmp_date).click()  
    #     time.sleep(1)
    #     self.driver.find_element(By.XPATH,"//span[text()='Set']").click()
    #     time.sleep(1)

    # def click_first_entry(self):
    #     time.sleep(5)  # Consider replacing with WebDriverWait
    #     first_entry = self.driver.find_element(By.XPATH, self.first_entry_css)
    #     first_entry.click()
    #     print("Extracted Name:", name_element.text)


