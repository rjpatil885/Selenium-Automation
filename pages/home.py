

from selenium.webdriver.common.by import By

from Base.BaseElement import *

from selenium.webdriver.common.alert import Alert
from Utility.utilityDriver import * 

class HomePage(Base_Element):

    text_alert1 = None 

    alert_button_home =  "//div[@class='card-body']//child::h5[text()='Alerts, Frame & Windows']"
    nav_alert_li_sl = "//*[text()='Alerts']"
    alert_button_sl = "//button[@id='alertButton']"
    alert_click_confirm_sl = "//button[@id='confirmButton']"
    alert_result_text_sl = "//span[@id='confirmResult']"
    alert_click_prompt_button_sl= "//button[@id='promtButton']"
    alert_prompt_text_sl = "//span[@id='promptResult']"


    u_qa = Utility_QA()

    def __init__(self, driver):
      self.driver = driver
      super(HomePage, self).__init__(driver)
    
    def alert_button_locator(self):

      val =  self.click(selector=self.alert_button_home)
      
      val.click()


    def Alert_nav_li(self):

      self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

      nav_li_alert = self.click(selector=self.nav_alert_li_sl)
    
      nav_li_alert.click()
     
    
    def Alert_click_text(self,text_alert1=None):
      
      self.alert_click_text = self.is_displayed_text(text_alert1)
      print(self.alert_click_text)
      
      return self.alert_click_text

    def Alert_click_button(self):
     
      alert_click_button = self.click(selector=self.alert_button_sl)
      
      alert_click_button.click()

      self.alert_box()

    def Alert_click_confirm_text(self,text_alert2=None):
      
      self.alert_click_confirm_button = self.is_displayed_text(text_alert2)


      return self.alert_click_confirm_button

    def Alert_click_confirm_button(self):
     
      alert_click_confirm_button = self.click(self.alert_click_confirm_sl)
      
      alert_click_confirm_button.click()

    def Alert_confirmed_result(self):
      
      self.alert_result_text = self.is_displayed(self.alert_result_text_sl)

      return self.alert_result_text

    def Alert_click_prompt_text(self,text_alert3=None):
        
      self.alert_click_prompt_text = self.is_displayed_text(text_alert3)
      
      return self.alert_click_prompt_text

    def Alert_click_prompt_button(self):
     
      alert_click_prompt_button = self.click(self.alert_click_prompt_button_sl)
      
      alert_click_prompt_button.click()

    def Alert_prompt_result(self):
      
      alert_prompt_text = self.is_displayed(self.alert_prompt_text_sl)
      
      return alert_prompt_text
      
    def Alert_box_prompt(self):

      self.alert_box()
    
    def Alert_box_args(self,data):

      self.send_keys_alert(data)


    def save_to_json(self):

      utl_qa = Utility_QA()
      
      dic_data ={
      
        'text1':self.alert_click_text.text,
        'text1_result': self.alert_result_text.text,
        'text2': self.alert_click_confirm_button.text,
        'text3':self.alert_click_prompt_text.text,

      }

      utl_qa.set_data (
        dic_data
      )
      
      
      
  
    # def send_keys(self, text):
    #   element = self.element
    #   element.clear()
    #   element.send_keys(text)

# class Product(BaseElement):
#     def __init__(self, driver, locator):
#         super(Product, self).__init__(driver, locator)

#     @property
#     def name(self):
#         element = self.element.find_element(By.CSS_SELECTOR, '.product-name')
#         return element.text

#     @property
#     def price(self):
#         element = self.element.find_element(By.CSS_SELECTOR, '.price-box .price')
#         price = element.text
#         return price




# # def __init__(self, driver):
#     super().__init__(driver)
#     self.driver = driver
#     self.logo = (By.ID, "logo")
#     self.login_account = (By.ID, "login_account")
#     self.login_password = (By.ID, "login_password")
#     self.login_button = (By.ID, "login_button")

# def is_logo_displayed(self):
#     return self.driver.find_element(*self.logo).is_displayed()

# def is_login_button_displayed(self):
#     return self.driver.find_element(*self.login_button).is_displayed()

# def input_username(self, username):
#     self.driver.find_element(*self.login_account).send_keys(username)

# def input_password(self, password):
#     self.driver.find_element(*self.login_password).send_keys(password)

# def click_login_button(self):