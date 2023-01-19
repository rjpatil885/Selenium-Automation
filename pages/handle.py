
from selenium.webdriver.common.by import By

from Base.BaseElement import *


class Handle(Base_Element):

    text_alert1 = None 
    alert_button_home =  "//div[@class='card-body']//child::h5[text()='Alerts, Frame & Windows']"
    nav_alert_li_sl = "//*[text()='Nested Frames']"

    browser_button =  "//span[text()='Browser Windows']"

    tab_button = "//button[@id='tabButton']"

    elements = "//*[text()='Elements']"

    links = "//span[text()='Links']"

    simple_list = "//a[@id='simpleLink']"

    def __init__(self, driver):

      self.driver = driver
      
      super(Handle, self).__init__(driver)
    
    def alert_button_locator(self):
     
      val =  self.click(selector=self.alert_button_home)
      val.click()

    def Alert_nav_li(self):

      self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
      browser_button = self.click(selector=self.browser_button)
      browser_button.click()

    
    def Tab_button(self):

      new_tab_button = self.click(self.tab_button)
      new_tab_button.click()
      self.driver.switch_to.window(self.driver.window_handles[-1])  
      self.page_text = self.driver.find_element(By.TAG_NAME, 'body').text
      self.driver.close()
      self.driver.switch_to.window(self.driver.window_handles[0])  
    
      return self.page_text   

    def Elements(self):

      self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
      
      element = self.click(self.elements)
      element.click()

      element = self.click(self.links)
      element.click()

      home_link = self.click(self.simple_list)
      home_link.click()
  
      self.driver.switch_to.window(self.driver.window_handles[0])  
    
      self.driver.close()
      self.driver.switch_to.window(self.driver.window_handles[-1])  
     

    def save_to_json(self):

          utl_qa = Utility_QA()
          dic_data ={

            'page_text':self.page_text,
       
          }

          utl_qa.set_data_handle (
            dic_data
          )